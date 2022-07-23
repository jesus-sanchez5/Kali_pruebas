#include <stdio.h>

int main(){

	setuid(0);
	printf("\n\n Listado de procesos (/usr/bin/ps)\n\n");
	system("/usr/bin/ps");
	printf("\n\n Listado procesos (ps)\n\n");
	system("ps");
	system("ping 8.8.8.8");
}
