void printf(char* str)
{
    unsigned short* VideoMemory = (unsigned short*)0xb8000;// variable declaration oxb8000 is position on screen //where to start
    for(int i = 0; str[i] != '\0'; ++i)
        VideoMemory[i] = (VideoMemory[i] & 0xFF00) | str[i];//0xff00 will remain color as it is // during execution
}

extern "C" void kernelMain(void* multiboot_structure,unsigned int magicnumber) // c linking
//style
{
    printf("Hello World!");

    while(1);// this runs the kernel forever so pc will not hang or crash
}
