as --gstabs+ -o useful_libc.o useful_libc.s
as --gstabs+ -o handCodeGen.o handCodeGen.s
gcc -static -o handCodeGen useful_libc.o handCodeGen.o
./handCodeGen
