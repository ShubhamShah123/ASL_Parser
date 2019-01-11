#---------------------------------------
# Get the file name without the last extension
baseName=${1%.*}
if [ "$baseName" = "" ]
then
  echo "Must specify the file base name."
  exit 1
fi

echo "#----------"
echo "# Compile/Assemble/Link/Run $baseName.asl"

#---------------------------------------
if [ -e $baseName.asl ]
then
  python3 hmwk_04.py $baseName.asl
  if [ $? -ne 0 ]; then
    echo "Analysis/Codegen error."
    exit 1
  else
    echo "Analysis/Codegen succeeded."
  fi

else
  echo "$baseName.asl did not exist."
  exit 1
fi

#---------------------------------------
if [ -e useful_libc.s ]
then
  as --gstabs+ -o useful_libc.o useful_libc.s
  if [ $? -ne 0 ]; then
    echo "useful_libc.s assembly error."
    exit 1
  else
    echo "useful_libc.s assembly succeeded."
  fi

else
  echo "useful_libc.s did not exist."
  exit 1
fi

#---------------------------------------
if [ -e $baseName.s ]
then
  as --gstabs+ -o $baseName.o $baseName.s
  if [ $? -ne 0 ]; then
    echo "$baseName.s assembly error."
    exit 1
  else
    echo "$baseName.s assembly succeeded."
  fi

else
  echo "$baseName.s did not exist."
  exit 1
fi

#---------------------------------------
gcc -static -o test useful_libc.o $baseName.o
if [ $? -ne 0 ]; then
  echo "$baseName.o linkage error."
  exit 1
else
  echo "$baseName.o linkage succeeded."
  rm useful_libc.o $baseName.o
fi

#---------------------------------------
echo -e "# Preparation complete.\n\n===== Running =====\n"
./test

#---------------------------------------
