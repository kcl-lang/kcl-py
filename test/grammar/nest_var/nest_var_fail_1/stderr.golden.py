import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(err_type=kcl_error.ErrType.CannotAddMembers_TYPE,
                            file_msgs=[
                                kcl_error.ErrFileMsg(
                                    filename=str(os.path.join(cwd, "main.k")),
                                    line_no=8,
                                    col_no=5,
                                    arg_msg="'err_name' is not defined in schema 'Name'"
                                ),
                            ],
                            arg_msg="Cannot add member 'err_name' to schema 'Name'")
    , file=sys.stdout
)

