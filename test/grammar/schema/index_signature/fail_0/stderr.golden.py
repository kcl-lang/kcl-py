
import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(
        err_type=kcl_error.ErrType.IndexSignatureError_TYPE,
        file_msgs=[
            kcl_error.ErrFileMsg(
                filename=str(os.path.join(cwd, "main.k")),
                line_no=3,
                col_no=5
            )
        ],
        arg_msg="the type 'int' of schema attribute 'label' does not meet the index signature definition [str]: str"
    ),
    file=sys.stdout
)

