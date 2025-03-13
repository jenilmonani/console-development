ENTRY(loader)             //This specifies the entry point of the program, which is where execution begins. In this case, it is labeled loader.
OUTPUT_FORMAT(elf32-i386)      //This line indicates the output format of the binary being created, which is ELF for a 32-bit x86 architecture.
OUTPUT_ARCH(i386:i386)        //This line specifies that the output architecture is for the i386 (32-bit x86) architecture.


SECTIONS
{
  . = 0x0100000;//set the start address

  .text :
  {
    *(.multiboot)// * means all files in current directory
    *(.text*)
    *(.rodata)//read only data that is sstring [rodata]
  }
  .data :
  {
    start_ctors = .;//start constructors
    KEEP(*( .init_array ));//This keeps the initialization functions from being discarded.
    KEEP(*(SORT_BY_INIT_PRIORITY( .init_array.* )));// This sorts and keeps initialization functions by priority.
    end_ctors = .;//end constructors

    *(.data)  //display data
  }
  .bss :
  {
    *(.bss)
  }

  /DISCARD/ :
  {
   *(.fini_array*)//This discards any .fini_array sections, which typically contain cleanup functions that run at program termination.
   *(.comment)//This discards any comment sections that might be included.

  }
}
