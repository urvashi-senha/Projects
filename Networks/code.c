#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h> 
#include<netdb.h>

int server_code(int server_port_no,char *type);
int client_code(int connect_port_no,char * type);
char srecv[1024],ssend[1024],crecv[1024],csend[1024];
char scommand[1024],scommand1[1024],scommand2[1024],scommand3[1024];
char ccommand[1024],ccommand1[1024],ccommand2[1024],ccommand3[1024];
int clarg = 0,sarg = 0;

typedef struct command_list
{
    char com[1024];
    struct command_list *next;
}command_list;

command_list *head=NULL;

void insert(char *data)
{
    command_list * temp;
    temp = (command_list*)malloc(sizeof(command_list));
    strcpy(temp -> com,data);
    temp->next=NULL;
    if(head!=NULL)
    {
	temp->next = head;
    }
	head=temp;
}

int client_input()
{
    gets(ccommand);
    printf("client received command %s\n",ccommand);

    insert(ccommand);    

    int i,j,k=0,l,flag =0,arg=0;

    for(i=0;ccommand[i]!='\0';i++)
    {
	if(ccommand[i] == ' ')
	{
	    flag =1;
	    break;
	}
	ccommand1[k++] = ccommand[i];
    }
    ccommand1[k] = '\0';
    arg++;
    k = 0;
    if(flag ==1)
    {
	flag = 0;
	for(j = i+1;ccommand[j]!= '\0';j++)
	{
	    if(ccommand[j] == ' ')
	    {
		flag =1;
		break;
	    }
	    ccommand2[k++] = ccommand[j];
	}
	ccommand2[k] = '\0';
	arg++;
    }
    k = 0;
    if(flag ==1)
    {
	flag = 0;
	for(l = j+1;ccommand[l]!= '\0';l++)
	{
	    if(ccommand[l] == ' ')
	    {
		flag =1;
		break;
	    }
	    ccommand3[k++] = ccommand[l];
	}
	ccommand3[k] = '\0';
	arg++;
    }
    return arg;
}

int server_input(char *scommand)
{

    printf("server received command %s\n",scommand);

    int i,j,k=0,l,flag =0,arg=0;

    for(i=0;scommand[i]!='\0';i++)
    {
	if(scommand[i] == ' ')
	{
	    flag =1;
	    break;
	}
	scommand1[k++] = scommand[i];
    }
    scommand1[k] = '\0';
    arg++;
    k = 0;
    if(flag ==1)
    {
	flag = 0;
	for(j = i+1;scommand[j]!= '\0';j++)
	{
	    if(scommand[j] == ' ')
	    {
		flag =1;
		break;
	    }
	    scommand2[k++] = scommand[j];
	}
	scommand2[k] = '\0';
	arg++;
    }
    k = 0;
    if(flag ==1)
    {
	flag = 0;
	for(l = j+1;scommand[l]!= '\0';l++)
	{
	    if(scommand[l] == ' ')
	    {
		flag =1;
		break;
	    }
	    scommand3[k++] = scommand[l];
	}
	scommand3[k] = '\0';
	arg++;
    }
    return arg;
}


int main()
{
    FILE *upload_file;
    upload_file = fopen("upload_command","w");
    fprintf(upload_file,"allow");
    fclose(upload_file);
    int server_port_no;
    int connect_port_no;
    char *type = (char *)malloc(sizeof(char) * 100);
    printf("Give your port no : ");
    scanf("%d",&server_port_no);
    printf("Give port no to connect : ");
    scanf("%d",&connect_port_no);
    printf("Type of transfer protocol : ");
    scanf("%s",type);
    pid_t pid;
    pid=fork();
    if(pid==-1)
    {
	printf("Error in creating Fork\n");
	exit(0);
    }
    if (pid==0) // Child process
    {
	server_code(server_port_no,type);
    }
    else // parent process
    {
	while(client_code(connect_port_no,type)>0)
	{
	    sleep(1);
	}
    }
    char temp[1024];
    sprintf(temp,"kill -9 %d",pid);
    system(temp);
    fflush(stdout);
    return 0;
}

int server_code(int server_port_no,char *type)
{
    int sock, connected, bytes=0 ;

    struct sockaddr_in server_addr,client_addr;
    int sin_size;

    if(strcmp(type,"tcp")==0)
    {

	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) 
	{
	    perror("Socket");
	    return 1;
	}
    }
    if(strcmp(type,"udp")==0)
    {

	if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1) 
	{
	    perror("Socket");
	    return 1;
	}
    }


    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port_no);
    server_addr.sin_addr.s_addr = INADDR_ANY;
    bzero(&(server_addr.sin_zero),8);

    if (bind(sock, (struct sockaddr *)&server_addr, sizeof(struct sockaddr))== -1) 
    {

	perror("Unable to bind");
	return 2;
    }

    if(strcmp(type,"tcp")==0)
    {
	if (listen(sock, 5) == -1) 
	{
	    perror("Listen");
	    return 3;
	}
    }
    if(strcmp(type,"tcp")==0)
	printf("\nTCPServer Waiting for client on port %d\n $ ",server_port_no);
    if(strcmp(type,"udp")==0)
	printf("\nUDPServer Waiting for client on port %d\n $ ",server_port_no);

    //fflush(stdout);


    while(1)
    {

	int bytes = 0;
	sin_size = sizeof(struct sockaddr_in);
	socklen_t * lol = (socklen_t *) &sin_size;
	if(strcmp(type,"tcp")==0)
	{
	    connected = accept(sock, (struct sockaddr *)&client_addr,lol);
	    printf("\n I got a connection from (%s , %d)\n $ ", inet_ntoa(client_addr.sin_addr),ntohs(client_addr.sin_port));
	}

	while (1)
	{
	    if(strcmp(type,"tcp")==0)
		bytes = recv(connected,srecv,1024,0);
	    if(strcmp(type,"udp")==0)
		bytes = recvfrom(sock,srecv,1024,0,(struct sockaddr *)&client_addr, lol);
	    srecv[bytes] = '\0';

	    sarg = server_input(srecv);

	    printf("bytes = %d scomand %s\nSccommand1 %s\n",bytes,scommand,scommand1);

	    if(bytes==0)
	    {
		printf("\nConnection closed by remote host\n");
		close(connected);
		break;
	    }
	    else if(scommand1[0]=='q' || scommand1[0]=='Q')
	    {
		printf("\nExiting...\n");
		close(connected);
		break;
	    }
	    else
	    {
		printf("\n RECIEVED DATA = %s \n $ " , srecv);
		if(sarg> 1 && strcmp(scommand1,"IndexGet") == 0)
		{
		    if(strcmp(scommand2,"LongList") == 0)
		    {
			char buffer1[1024],filedata[1024];
			FILE *fp1,*fp2,*fp3;
			system("touch file1");
			system("ls -l | wc -l > file1");
			//fflush(stdout);
			fp1 = fopen("file1","r");
			fgets(buffer1,1024,fp1);
			int lines = atoi(buffer1);
			lines--;
			if(strcmp(type,"tcp") == 0)
			    send(connected,&lines,sizeof(int),0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,&lines,sizeof(int),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			buffer1[0]= '\0';

			sprintf(buffer1,"ls -l --time-style=+%y%m%d%H%M%S -t | tail -%d | awk '{print $7}' > file2",lines);
			system(buffer1);

			char buf[1024],filedate[1024],filedat[1024];
			char n[1024];
			fp2 = fopen("file2","r");

			int o;

			while(fgets(buffer1,1024,fp2))
			{
			    for(o=0;o<strlen(buffer1)-1;o++)
				n[o] = buffer1[o];
			    n[o] = '\0';
			    if(strcmp(n,"file2") != 0)
			    {

				//			printf("here\n");
				strcpy(filedata,"Name: ");
				strcat(filedata,buffer1);
							printf("checking %s",filedata);
				if(strcmp(type,"tcp") == 0)
				    send(connected,filedata,strlen(filedata),0);
				else if(strcmp(type,"udp") == 0)
				    sendto(sock,filedata,strlen(filedata),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

				sprintf(buf,"ls -l %s | tail -%d | awk '{print $5}'> file3",n,lines);
				system(buf);

				fp3 = fopen("file3","r");
				fgets(buf,1024,fp3);
				fclose(fp3);
				strcpy(filedat,"Size: ");
				strcat(filedat,buf);
				//			printf("%s\n",filedat);
				if(strcmp(type,"tcp") == 0)
				    send(connected,filedat,strlen(filedat),0);
				else if(strcmp(type,"udp") == 0)
				    sendto(sock,filedat,strlen(filedat),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

				/*			sprintf(buf,"ls -l %s --time-style=+%y%m%d -t | tail -%d | awk '{print $6}'> file3",n,lines);
							system(buf);
							fp3 = fopen("file3","r");
							fgets(buf,1024,fp3);
							fclose(fp3);
							strcpy(filedate,"Date: ");
							strcat(filedate,buf);
				//			printf("%s\n",buf);
				if(strcmp(type,"tcp") == 0)
				send(connected,filedate,strlen(filedate),0);
				else if(strcmp(type,"udp") == 0)
				sendto(sock,filedate,strlen(filedate),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
				 */			
				for(o=0;o<strlen(buffer1);o++)
				    n[o] = buffer1[o] = '\0';

			    }
			}

		    }
		    else if(sarg> 2 && strcmp(scommand2,"regEx") == 0)
		    {
			printf("server in regev %s\n",scommand3);
			char buffer[1024],buf[1024];
			sprintf(buffer,"ls %s > file",scommand3);
			system(buffer);
			FILE *f,*f1;
			f = fopen("file","r");

			system("ls file | wc -l > lin");

			f1 = fopen("lin","r");
			fgets(buffer,1024,f1);
			int lines = atoi(buffer);

			if(strcmp(type,"tcp") == 0)
			    send(connected,&lines,sizeof(int),0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,&lines,sizeof(int),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			while(fgets(buffer,1024,f))
			{
			    if(strcmp(type,"tcp") == 0)
				send(connected,buffer,strlen(buffer),0);
			    else if(strcmp(type,"udp") == 0)
				sendto(sock,buffer,strlen(buffer),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			}

		    }
		    else if(sarg < 2 && strcmp(scommand2,"regEx") == 0)
		    {
			strcpy(ssend,"Invalid Syntax\nIndexGet regEx <expression>\n $");
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
		    }

		}
		else if(strcmp(scommand1,"IndexGet") ==0 && sarg < 1)
		{
		    strcpy(ssend,"Invalid Syntax\n1. IndexGet LongList\n2. IndexGet regEx <expression>\n $");
		    if(strcmp(type,"tcp") == 0)
			send(connected,ssend,1024,0);
		    else if(strcmp(type,"udp") == 0)
			sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
		}
		else if(sarg > 1 && strcmp(scommand1,"Download") == 0)
		{
		    if(access(scommand2,F_OK) == -1)
		    {
			strcpy(ssend,"File does not exist in this directory\n $");
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
			strcpy(ssend,"incorrect md5sum\n $");
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
			if(strcmp(type,"tcp")==0)
			    bytes = recv(connected,srecv,1024,0);
			if(strcmp(type,"udp")==0)
			    bytes = recvfrom(sock,srecv,1024,0,(struct sockaddr *)&client_addr, lol);
		    }
		    else
		    {
			char buffer[1024];
			strcpy(ssend,"File exists\n $");
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			sprintf(buffer,"md5sum %s | awk '{print $1}' > mdsum",scommand2);
			system(buffer);

			char buffer1[1024];	
			FILE *f=fopen("mdsum","r");
			fgets(buffer1,1024,f);
			fclose(f);

			strcpy(ssend,buffer1);
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			if(strcmp(type,"tcp")==0)
			    bytes = recv(connected,srecv,1024,0);
			if(strcmp(type,"udp")==0)
			    bytes = recvfrom(sock,srecv,1024,0,(struct sockaddr *)&client_addr, lol);
			srecv[bytes] = '\0';

			if(srecv[0]=='O')
			{
			    printf("OKKKK\n");
			    FILE *fp,*fp2;
			    char buf[1024];
			    sprintf(buf,"ls %s | wc -l >lin",scommand2);
			    system(buf);

			    fp2 = fopen("lin","r");
			    fgets(buf,1024,fp2);

			    int lines = atoi(buf);
			    if(strcmp(type,"tcp") == 0)
				send(connected,&lines,sizeof(int),0);
			    else if(strcmp(type,"udp") == 0)
				sendto(sock,&lines,sizeof(int),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
			    char filedata[1024];

			    fp = fopen(scommand2,"r");
			    while(fgets(filedata,1024,fp))
			    {
				if(strcmp(type,"tcp") == 0)
				    send(connected,filedata,strlen(filedata),0);
				else if(strcmp(type,"udp") == 0)
				    sendto(sock,filedata,strlen(filedata),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
			    }

			}
		    }
		}


		else if(sarg < 1 && strcmp(scommand1,"Download") == 0)
		{
		    strcpy(ssend,"Invalid Syntax\nDownload  <filename>\n $");
		    if(strcmp(type,"tcp") == 0)
			send(connected,ssend,1024,0);
		    else if(strcmp(type,"udp") == 0)
			sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

		}
		else if(sarg == 2 && strcmp(scommand1,"FileHash") == 0 && strcmp(scommand2,"Verify") == 0)
		{
		    strcpy(ssend,"Invalid Syntax\nFileHash Verify <filename>\n $");
		    if(strcmp(type,"tcp") == 0)
			send(connected,ssend,1024,0);
		    else if(strcmp(type,"udp") == 0)
			sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));
		}
		else if(sarg > 2 && strcmp(scommand1,"FileHash") == 0 && strcmp(scommand2,"Verify") == 0)
		{
		    if(strcmp(scommand2,"Verify") == 0)
		    {
			char buffer[1024];
			sprintf(buffer,"md5sum %s | awk '{print $1}' > mdsum",scommand3);
			system(buffer);

			FILE *fp = fopen("mdsum","r");

			fgets(ssend,1024,fp);
			if(strcmp(type,"tcp") == 0)
			    send(connected,ssend,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));


		    }
		}
		else if(sarg < 2 && strcmp(scommand1,"FileHash")==0 )
		{
		    strcpy(ssend,"Invalid Syntax\nFileHash CheckAll\n $");
		    if(strcmp(type,"tcp") == 0)
			send(connected,ssend,1024,0);
		    else if(strcmp(type,"udp") == 0)
			sendto(sock,ssend,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

		}
		else if(sarg >1 && strcmp(scommand1,"FileHash")==0 && strcmp(scommand2,"CheckAll")==0 )
		{
		    printf("server checkall\n");
		    char buffer1[1024],filedata[1024];
		    FILE *fp1,*fp2,*fp3;
		    system("touch file1");
		    system("ls -l | wc -l > file1");
		    //fflush(stdout);
		    fp1 = fopen("file1","r");
		    fgets(buffer1,1024,fp1);
		    int lines = atoi(buffer1);
		    lines--;
		    if(strcmp(type,"tcp") == 0)
			send(connected,&lines,sizeof(int),0);
		    else if(strcmp(type,"udp") == 0)
			sendto(sock,&lines,sizeof(int),0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

		    buffer1[0]= '\0';

		    char t[1024];

		    sprintf(t,"ls -l | tail -%d | awk '{print $9}' > file2",lines);
		    system(t);

		    fp2 = fopen("file2","r");
		    char filename[1024],command[1024],f[1024];
		    int o;


		    while(fgets(filename,1024,fp2))
		    {
			    for(o=0;o<strlen(filename)-1;o++)
			    {
				f[o] = filename[o];
				//printf("f[%d] %c\n",o,f[o]);
			    }
			    f[o] = '\0';
			printf("file2 line %s ", f);
			if(strcmp(type,"tcp") == 0)
			    send(connected,filename,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,filename,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

			sprintf(command,"md5sum %s | awk '{print $1}' > file3",f);
			system(command);
			fp3 = fopen("file3","r");
			fgets(filedata,1024,fp3);

			if(strcmp(type,"tcp") == 0)
			    send(connected,filedata,1024,0);
			else if(strcmp(type,"udp") == 0)
			    sendto(sock,filedata,1024,0,(struct sockaddr *)&client_addr, sizeof(struct sockaddr));

		    }

		}

	    }


	}
	fflush(stdout);
    }
    close(sock);
    return 0;
}
int client_code(int connect_port_no,char * type)
{
    int sock, bytes =0 ;
    struct hostent *host;
    struct sockaddr_in server_addr;

    host = gethostbyname("127.0.0.1");
    if(strcmp(type,"tcp")==0)
    {
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) 
	{
	    perror("Socket");
	    return 1;
	}
    }
    if(strcmp(type,"udp")==0)
    {
	if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1) 
	{
	    perror("Socket");
	    return 1;
	}
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(connect_port_no);
    memcpy(&server_addr.sin_addr,host -> h_addr, host->h_length);
    bzero(&(server_addr.sin_zero),8);
    int sin_size = sizeof(struct sockaddr_in);
    socklen_t * lol = (socklen_t *) &sin_size;
    if(strcmp(type,"tcp")==0)
    {
	if (connect(sock, (struct sockaddr *)&server_addr,sizeof(struct sockaddr)) == -1) 
	{
	    perror("Connect");
	    return 2;
	}
	printf("\n CLIENT : Connected to Port No %d\n",connect_port_no);
    }

    do
    {
	clarg = client_input();

	printf("ccommand %s\nccommand1 %s\n",ccommand,ccommand1);

	if(clarg > 1)
	{
	    if(strcmp(ccommand1,"IndexGet") == 0)
	    {
		if(strcmp(ccommand2,"LongList") == 0)
		{
		    int i,lines =0 ;
		    if(strcmp(type,"tcp")==0)
			send(sock,ccommand,strlen(ccommand),0);
		    else
			sendto(sock,ccommand,strlen(ccommand),0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));
		    if(strcmp(type,"tcp")==0)
			recv(sock,&lines,sizeof(int),0);
		    else
			recvfrom(sock,&lines,sizeof(int),0,(struct sockaddr *)&server_addr,lol);

		    printf("lines: %d\n",lines);
		    for(i=0;i<lines;i++)
		    {
			//		    printf("for\n");
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';
			printf("%s",crecv);
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';
			printf("%s",crecv);
			/*		if(strcmp(type,"tcp")==0)
					bytes = recv(sock,crecv,1024,0);
					else
					bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
					crecv[bytes] = '\0';
			 */		printf("%s",crecv);
		    }
		}
		else if(strcmp(ccommand2 ,"regEx") == 0)
		{
		    if(strcmp(type,"tcp")==0)
			send(sock,ccommand,strlen(ccommand),0);
		    else
			sendto(sock,ccommand,strlen(ccommand),0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));
		    printf("in regev\n");
		    int lines=0;
		    if(strcmp(type,"tcp")==0)
			recv(sock,&lines,sizeof(int),0);
		    else
			recvfrom(sock,&lines,sizeof(int),0,(struct sockaddr *)&server_addr,lol);

		    printf("lines : %d\n",lines);

		    int i;
		    for(i=0;i<lines;i++)
		    {
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';
			printf("%s",crecv);
		    }

		}
	    }
	    else if(strcmp(ccommand1,"Download")==0)
	    {
		if(strcmp(type,"tcp")==0)
		    send(sock,ccommand,strlen(ccommand),0);
		else
		    sendto(sock,ccommand,strlen(ccommand),0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));
		printf("in download\n");
		//file existence
		if(strcmp(type,"tcp")==0)
		    bytes = recv(sock,crecv,1024,0);
		else
		    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
		crecv[bytes] = '\0';
		printf("%s",crecv);
		//md5sum
		if(strcmp(type,"tcp")==0)
		    bytes = recv(sock,crecv,1024,0);
		else
		    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
		crecv[bytes] = '\0';
		printf("%s",crecv);

		char buffer[1024],buffer1[1024];
		sprintf(buffer,"md5sum %s | awk '{print $1}' > md",ccommand2);
		system(buffer);
		FILE *f;
		f=fopen("md","r");
		fgets(buffer1,1024,f);

		printf("%s",buffer1);

		int j,flag=0;
		char temp[1024],t[1024];
		for(j=0;j<32;j++)
		{
		    if(crecv[j] != buffer1[j])
		    {
			flag = 1;
			break;
		    }

		}


		if(flag == 0)
		{
		    printf("OK sent\n");
		    strcpy(csend,"OK");
		    if(strcmp(type,"tcp")==0)
			send(sock,csend,1024,0);
		    else
			sendto(sock,csend,1024,0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));

		    int lines =0;
		    if(strcmp(type,"tcp")==0)
			recv(sock,&lines,sizeof(int),0);
		    else
			recvfrom(sock,&lines,sizeof(int),0,(struct sockaddr *)&server_addr,lol);

		    printf("lines : %d\n",lines);

		    int i;
		    FILE *fp;
		    fp = fopen(ccommand2,"w+");
		    for(i=0;i<lines;i++)
		    {
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';

			fputs(crecv,fp);
			//		    printf("%s",crecv);
		    }
		    printf("File recieved !!!\n");

		}

	    }
	    else if(strcmp(ccommand1,"FileHash")==0)
	    {
		if(strcmp(ccommand2,"Verify")==0)
		{
		    if(strcmp(type,"tcp")==0)
			send(sock,ccommand,strlen(ccommand),0);
		    else
			sendto(sock,ccommand,strlen(ccommand),0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));
		    printf("in filehash\n");

		    if(strcmp(type,"tcp")==0)
			bytes = recv(sock,crecv,1024,0);
		    else
			bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
		    crecv[bytes] = '\0';
		    printf(" %s md5sum : %s\n",ccommand3,crecv);
		}
		else if(strcmp(ccommand2,"CheckAll") == 0)
		{
		    if(strcmp(type,"tcp")==0)
			send(sock,ccommand,strlen(ccommand),0);
		    else
			sendto(sock,ccommand,strlen(ccommand),0,(struct sockaddr *)&server_addr,sizeof(struct sockaddr));
		    printf("in filehashcheckall\n");
		    int lines =0,i;
		    if(strcmp(type,"tcp")==0)
			recv(sock,&lines,sizeof(int),0);
		    else
			recvfrom(sock,&lines,sizeof(int),0,(struct sockaddr *)&server_addr,lol);

		    printf("lines : %d\n",lines);
		    for(i=0;i<lines;i++)
		    {
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';

			printf("%s",crecv);
			if(strcmp(type,"tcp")==0)
			    bytes = recv(sock,crecv,1024,0);
			else
			    bytes = recvfrom(sock,crecv,1024,0,(struct sockaddr *)&server_addr,lol);
			crecv[bytes] = '\0';
			printf("%s",crecv);

		    }

		}
	    }
	}
	else
	    continue;    

    }while(ccommand[0]!='q' || ccommand[0]!='Q');

    return 0;
}

