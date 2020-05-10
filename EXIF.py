#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Library to extract Exif information from digital camera image files.
# https://github.com/ianare/exif-py
#
#
# Copyright (c) 2002-2007 Gene Cash
# Copyright (c) 2007-2014 Ianaré Sévi and contributors
# Copyright (c) 2020-     Cyb3r Jak3
#
# See LICENSE.txt file for licensing information
# See ChangeLog.rst file for all contributors and changes
#

"""
Runs Exif tag extraction in command line.
"""

import sys
import argparse
import timeit
from exifreader.tags import DEFAULT_STOP_TAG, FIELD_TYPES
from exifreader import process_file, exif_log, __version__

logger = exif_log.get_logger()


def show_version():
    """Show the program version."""
    print('Version %s on Python %s' % (__version__, sys.version[0:5]))
    sys.exit(0)


def parse_arguments():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(
        description="Library to extract Exif information from digital camera image files.")

    parser.add_argument('files', nargs='*', default=None,
                        help='Path of photos to check.')
    parser.add_argument(
        "-v", "--version", action="store_true", default=False,
        help="Display version information and exit.")
    parser.add_argument(
        "-q", "--quick", action="store_false", dest="detailed", default=True,
        help="Do not process MakerNotes")
    parser.add_argument(
        "-t", "--stop-tag", default=DEFAULT_STOP_TAG,
        help="Stop processing when this tag is retrieved."
    )
    parser.add_argument(
        "-s", "--strict", action="store_true", default=False,
        help="Run in strict mode (stop on errors)."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False,
        help="Run in debug mode"
    )

    return parser.parse_args()


def main():
    """Parse command line options/arguments and execute."""
    args = parse_arguments()

    if args.version:
        show_version()

    exif_log.setup_logger(args.debug)

    # output info for each file
    for filename in args.files:
        file_start = timeit.default_timer()
        try:
            img_file = open(str(filename), 'rb')
        except IOError:
            logger.error("'%s' is unreadable", filename)
            continue
        logger.info("Opening: %s", filename)

        tag_start = timeit.default_timer()

        # get the tags
        data = process_file(
            img_file,
            stop_tag=args.stop_tag,
            details=args.detailed,
            strict=args.strict,
            debug=args.debug)

        tag_stop = timeit.default_timer()

        if not data:
            logger.warning("No EXIF information found\n")
            continue

        if 'JPEGThumbnail' in data:
            logger.info('File has JPEG thumbnail')
            del data['JPEGThumbnail']
        if 'TIFFThumbnail' in data:
            logger.info('File has TIFF thumbnail')
            del data['TIFFThumbnail']

        tag_keys = list(data.keys())
        tag_keys.sort()

        for i in tag_keys:
            logger.info('%s (%s): %s', i, FIELD_TYPES[data[i].field_type][2], data[i].printable)

        file_stop = timeit.default_timer()

        logger.debug("Tags processed in %s seconds", tag_stop - tag_start)
        logger.debug("File processed in %s seconds", file_stop - file_start)
        print("")


if __name__ == '__main__':
    main()
