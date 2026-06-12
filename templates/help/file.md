title: file

determines the type of a file as ASCII text

	file /dev/sda
`/dev/sda:   block special` says,its a block device.

>`Tips and tricks:`

You can also find about file system details of special devices.

	file -s /dev/sda2

says
	/dev/sda2: x86 boot sector, code offset 0x52, OEM-ID "NTFS    ", 
	sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, 
	heads 255, hidden sectors 161792, dos &lt; 4.0 BootSector (0x80)

often we need to find the location of a certain file

	whereis ls
