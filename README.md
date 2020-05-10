# ExifReader

**Fork of Exif.py from [ianare](https://github.com/ianare/exif-py) and used under BSD License**

Easy to use Python module to extract Exif metadata from tiff and jpeg files.

Originally written by Gene Cash & Thierry Bousch.

## Installation

### PyPi

The recommend process is into install exifreader from the [PyPi package](https://pypi.org/project/exifreader)
See the [pip documentation](https://pip.pypa.io/en/latest/user_guide.html) for more info.

## Compatibility

Exifreader is tested and officially supported on the following Python versions:

- 3.5 *Support will likely be removed in future releases*
- 3.6
- 3.7
- 3.8

## Usage

### Command line

Some examples:

```bash
EXIF.py image1.jpg
EXIF.py image1.jpg image2.tiff
find ~/Pictures -name "*.jpg" -name "*.tiff" | xargs EXIF.py
```

Show command line options

```bash
EXIF.py --help
```

### Python Script

```python
import exifread
    # Open image file for reading (binary mode)
    f = open(path_name, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
```

Returned tags will be a dictionary mapping names of Exif tags to their
values in the file named by path_name.
You can process the tags as you wish. In particular, you can iterate through all the tags with

```python
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print "Key: %s, value %s" % (tag, tags[tag])
```

An ``if`` statement is used to avoid printing out a few of the tags that tend to be long or boring.

The tags dictionary will include keys for all of the usual Exif tags, and will also include keys for
Makernotes used by some cameras, for which we have a good specification.

Note that the dictionary keys are the IFD name followed by the tag name. For example::
'EXIF DateTimeOriginal', 'Image Orientation', 'MakerNote FocusMode'

## Tag Descriptions

Tags are divided into these main categories:

- ``Image``: information related to the main image (IFD0 of the Exif data).
- ``Thumbnail``: information related to the thumbnail image, if present (IFD1 of the Exif data).
- ``EXIF``: Exif information (sub-IFD).
- ``GPS``: GPS information (sub-IFD).
- ``Interoperability``: Interoperability information (sub-IFD).
- ``MakerNote``: Manufacturer specific information. There are no official published references for these tags.

## Processing Options

These options can be used both in command line mode and within a script.

### Faster Processing

Don't process makernotes tags, don't extract the thumbnail image (if any).

Pass the ``-q`` or ``--quick`` command line arguments, or as

```python
    tags = exifread.process_file(f, details=False)
```

### Stop at a Given Tag

To stop processing the file after a specified tag is retrieved.

Pass the ``-t TAG`` or ``--stop-tag TAG`` argument, or as

```python
    tags = exifread.process_file(f, stop_tag='TAG')
```

where ``TAG`` is a valid tag name, ex ``'DateTimeOriginal'``.

**The two above options are useful to speed up processing of large numbers of files.**

### Strict Processing

Return an error on invalid tags instead of silently ignoring.

Pass the ``-s`` or ``--strict`` argument, or as::

```python
    tags = exifread.process_file(f, strict=True)
```
