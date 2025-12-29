# File Upload Error Fix

## Error Encountered
```
File errors: ['Failed to save file IMG_20250921_210909.jpg: null …0e, 7e342c9e-c3f5-450b-9e93-f963777dbb80, null).\n']
```

## Root Cause Analysis
The error suggests a database constraint violation. The error format with UUIDs and "null" values indicates:
1. Possible NULL constraint violation on a required field
2. Foreign key constraint issue
3. File name validation issue

## Fixes Applied

### 1. **File Name Validation & Sanitization**
   - Added validation to ensure file name is never empty or None
   - Added fallback to generate a name if file name is missing
   - Added truncation for file names exceeding 255 characters (database limit)
   - Preserves file extension when truncating

### 2. **File Content Validation**
   - Validates file has content (size > 0) before attempting to save
   - Skips empty files with a warning instead of failing

### 3. **Enhanced Error Logging**
   - Logs file details before saving (name, size, assignment, user)
   - Logs full error traceback for debugging
   - Provides more detailed error messages to client

### 4. **Explicit Field Validation**
   - Validates all required fields before saving
   - Uses model instance creation instead of `.create()` for better control
   - Explicitly checks assignment, file_name, and file object

## Code Changes

### Before:
```python
file_obj = AssignmentFile.objects.create(
    assignment=assignment,
    uploaded_by=request.user,
    file=f,
    file_name=f.name,
    file_type='support'
)
```

### After:
```python
# Validate and sanitize file name
file_name = getattr(f, 'name', None) or 'unnamed_file'
if not file_name or file_name.strip() == '':
    file_name = f'file_{uploaded_file_count + 1}'

# Truncate if too long
if len(file_name) > 255:
    name, ext = os.path.splitext(file_name)
    if ext:
        file_name = name[:255-len(ext)] + ext
    else:
        file_name = file_name[:255]

# Validate file has content
if not hasattr(f, 'size') or f.size == 0:
    error_msg = f"File {file_name} is empty (0 bytes)"
    logger.warning(error_msg)
    file_errors.append(error_msg)
    continue

# Create with explicit validation
file_obj = AssignmentFile(
    assignment=assignment,
    uploaded_by=request.user,
    file=f,
    file_name=file_name,
    file_type='support'
)

# Validate required fields
if not file_obj.assignment:
    raise ValueError("Assignment is required")
if not file_obj.file_name or file_obj.file_name.strip() == '':
    raise ValueError("File name is required")
if not file_obj.file:
    raise ValueError("File object is required")

# Save
file_obj.save()
```

## Testing Steps

1. **Test with normal file**:
   - Upload a file with a normal name (e.g., "document.pdf")
   - Should save successfully

2. **Test with long filename**:
   - Upload a file with a very long name (>255 chars)
   - Should truncate and save

3. **Test with missing filename**:
   - Upload a file without a name (if possible)
   - Should generate a fallback name

4. **Test with empty file**:
   - Upload an empty file (0 bytes)
   - Should skip with warning, not fail

5. **Check server logs**:
   - Look for detailed file information before saving
   - Check for any validation errors

## Expected Behavior

- Files with valid names should save successfully
- Files with long names should be truncated
- Files without names should get generated names
- Empty files should be skipped with a warning
- All errors should be logged with full details

## If Error Persists

1. Check server logs for the full error traceback
2. Verify database permissions for the `assignment_files` table
3. Check if MEDIA_ROOT is properly configured
4. Verify file storage backend settings
5. Check for database-level constraints that might conflict

## Additional Debugging

If the error continues, check:
- Database schema for `assignment_files` table
- Any triggers or constraints on the table
- File storage backend configuration
- MEDIA_ROOT permissions and path

