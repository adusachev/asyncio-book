# #!/bin/bash


# filename="file-01*.txt"

# # Argument parser
# while [ $# -gt 0 ]
# do
#     case $1 in
#         --name|-n)
#             file_description=$2;
#             shift 2
#             ;;
#         *)
#         echo -e "ERROR: Unknown command line parameter \n" >&2
#         exit 1
#         ;;
#     esac
# done


# num=0
# while [ -f $filename ]; do
#     num=$(( $num + 1 ))
#     filename="file-${num}.txt"
# done

# # create new file
# touch $filename

# # add contents to file
# cat << EOF >> $filename
# import asyncio
# from util import async_timed, delay


# EOF