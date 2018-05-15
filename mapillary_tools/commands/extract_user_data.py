import os
import sys

from mapillary_tools.process_user_properties import process_user_properties


class Command:
    name = 'extract_user_data'
    help = "Extract user data."

    def add_arguments(self, parser):

        # command specific args
        # organization level parameters
        parser.add_argument(
            '--organization_name', help="Specify organization name", default=None, required=False)
        parser.add_argument(
            '--organization_key', help="Specify organization key", default=None, required=False)
        parser.add_argument('--private',
                            help="Specify whether the import is private", action='store_true', default=False, required=False)

    def run(self, args):

        # basic check for all
        import_path = os.path.abspath(args.path)
        if not os.path.isdir(import_path):
            print("Error, import directory " + import_path +
                  " doesnt not exist, exiting...")
            sys.exit()

        process_user_properties(import_path,
                                args.user_name,
                                args.organization_name,
                                args.organization_key,
                                args.private,
                                args.master_upload,
                                args.verbose,
                                args.rerun,
                                args.skip_subfolders)
