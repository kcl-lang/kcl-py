import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(err_type=kcl_error.ErrType.TypeError_Compile_TYPE,
                            file_msgs=[
                                kcl_error.ErrFileMsg(
                                    filename=str(os.path.join(cwd, "main.k")),
                                    line_no=3,
                                    col_no=5,
                                    arg_msg="expect str",
                                    err_level=kcl_error.ErrLevel.ORDINARY
                                ),
                                kcl_error.ErrFileMsg(
                                    filename=str(os.path.join(cwd, "main.k")),
                                    line_no=15,
                                    col_no=17,
                                    arg_msg="got int(123)"
                                ),
                            ],
                            arg_msg='expect str, got int(123)')
    , file=sys.stdout
)

