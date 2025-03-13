.set MAGIC,0x1badb002  //position and standard magic number for multiboot
.set FLAGS,(1<<0 | 1<<1) // flag is bitwise or indicating features
.set CHECKSUM,-(MAGIC + FLAGS) //check for negative sum

.section .multiboot
    .long MAGIC
    .long FLAGS
    .long CHECKSUM

.section .text //entry point for loader
.extern kernelMain
.global loader

loader: //sets up the stack for kernel pushes register eax and ebx onto stack
    mov $kernel_stack,%esp
    push %eax
    push %ebx
    call kernelMain

_stop: // infinite loop to hold the cpu
    cli   
    hlt  //halt the screen
    jmp _stop


.section .bss
.space 2*1024*1024; //bss section reserves 2mb space likely for kernels use.
kernel_stack:
