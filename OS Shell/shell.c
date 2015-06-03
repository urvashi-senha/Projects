/**************************************
Special commands : 
jobs - lists all jobs
kjob = kill job
fg - made into a foreground process
pinfo - process info
overkill - kill all processes
**************************************/
/******Libraries*****/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <unistd.h>
#include<sys/types.h>
#include<signal.h>
#include<wait.h>
#include<fcntl.h>
/********************/
typedef struct node		//structure to store all the
{				//background processes
    char name[1000];
    int status;
    int pid;
}node;
node all[1000];			//array of node to store the  processes
int all_count=0;
node back[1000];		//array of nodes to store the background processes
int back_count=0;

int parent_pid;
char *HOME;

/******* Functions ****************/
void signal_handler(int signum);
void child_handler(int signum);
void print_cmd_line();
void store_input(int*,int*,int*,int*,int*,char*);
int redirect_parse(const char *,char *, char **);
void redirect_input_output(char *);
void pipe_handling(char *);
void break_input(char*,int*,char**);
void command_cd(char**);
void command_jobs();
void command_kjob(char*,char*);
void command_fg(char*);
void command_pinfo_1(pid_t,int);
void command_pinfo_2(char*);
void command_overkill();
void exec_cmds(char* ,char**,pid_t,int,int);
void exec_external(char*,char**,int);
/************************************/

/******* Main Function **************/
int main()
{
    signal(SIGINT,SIG_IGN);			//Signal handling
    signal(SIGINT,signal_handler);
    signal(SIGCHLD,SIG_IGN);
    signal(SIGCHLD,child_handler);
    signal(SIGTSTP,SIG_IGN);
    signal(SIGTSTP,signal_handler);
    signal(SIGQUIT,SIG_IGN);
    signal(SIGQUIT,signal_handler);

    HOME=getenv("PWD");				//Stores the directory where ./a.out is executing
    pid_t pid_of_this=getpid();			//Stores ./a.out process id
    while(1)
    {
	print_cmd_line();			//Calling the function to print the command line

	int i=0,j=0,space=0,t=0;
	int backgrnd_flag=0,pipe_flag=0,in_redirect_flag=0,out_redirect_flag=0,cmds=0,count=0;

	int *bf=&backgrnd_flag,*pf=&pipe_flag,*irf=&in_redirect_flag,*orf=&out_redirect_flag,*cm=&cmds,*cn=&count;

	char input[5000],*arr[5000],input2[5000];

	store_input(bf,pf,irf,orf,cn,input);		//Calling function to scan the input

	//	printf("input-->%s\n",input);

	if((in_redirect_flag==1 || out_redirect_flag==1) && (pipe_flag==0)) 
	    redirect_input_output(input);
	else if(pipe_flag==1)
	    pipe_handling(input);
	else
	{
	    strcpy(input2,input);
	    if(strcmp(input2,"\0"))
	    {
		break_input(input2,cm,arr);			//Calling function to break the input according to spaces
		/*	for(i=0;arr[i]!='\0';i++)
			printf("%s\n",arr[i]);
		 */
		//		printf("arr[0]-->%s\n",arr[0]);

		exec_cmds(input,arr,pid_of_this,count,backgrnd_flag);	//Calling function to execute the command
	    }
	}
    }
    return 0;
}
/************* End of Main Function **************/

//Function to print the command line
void print_cmd_line()
{
    char user[1000],system[1000],*path,cwd[5000];
    int r;

    r=getlogin_r(user,1000);
    gethostname(system,1000);
    getcwd(cwd,5000);
    path=strstr(cwd,HOME);
    if(strlen(HOME)>strlen(cwd))
	printf("%s@%s:~%s>",user,system,cwd);
    else
    {
	path=path+strlen(HOME);
	printf("%s@%s:~%s>",user,system,path);
    }
    return;
}
//Function to scan and save the command
void store_input(int *bf,int *pf,int *irf,int *orf,int *cn,char input[])
{
    char final_input[5000]={'\0'},c;
    int i=0,spaces=0,j=0;

    scanf("%c",&c);
    while(c!='\n')
    {
	if(c=='|')
	    *pf=1;
	else if(c=='<')
	    *irf=1;
	else if(c=='>')
	    *orf=1;
	if(c=='&')
	{
	    *bf=1;
	    i--;
	}
	else
	    input[i++]=c;

	scanf("%c",&c);
    }
    input[i]='\0';

    while(input[spaces]==' '||input[spaces]=='\t')
	spaces++;
    while(input[j]!='\0')
	final_input[j++]=input[spaces++];
    final_input[j]='\0';
    int k;
    for(k=0;k<j;k++)
	input[k]=final_input[k];
    input[j]='\0';
    *cn=j;
    return;
}

//Function to break the input according to space
void break_input(char *input2,int* cm,char *arr[])
{
    char *pieces;
    int count=0;

    pieces=strtok(input2," ");
    while(pieces!=NULL)
    {
	pieces[strlen(pieces)]='\0';
	arr[count++]=pieces;
	pieces=strtok(NULL," ");
    }
    arr[count++]=pieces;
    (*cm)=count;
    return; 
}
//Function to execute the cd command
void command_cd(char* arr[])
{
    char cwd[1000],current[1000];
    /*    if(arr[1]!=NULL)
	  {
	  if(arr[1][0]=='.' && arr[1][1]=='.' && arr[1][2]=='\0')
	  {
	  getcwd(cwd,1000);
	  if(strlen(HOME)>=strlen(cwd))
	  {
	  chdir(cwd);
	  return;
	  }
	  }
	  }
     */
    if((arr[1]==NULL) || (!(strcmp,arr[1],"~")) ||(!strcmp(arr[1],"~/")))
    {
	if(chdir(HOME)!=0)
	    perror("chdir()");
	return;
    }
    else
    {
	chdir(arr[1]);
    }
    return;

    /*etcwd(cwd,1000);
      strcat(cwd,"/");
      int len=strlen(cwd)+strlen(arr[1])+1;
      if(arr[1]!=NULL)
      strcat(cwd,arr[1]);
      cwd[len]='\0';
      if((chdir(cwd))!=0)
      perror("chdir()");
      else
      return;
     */
}

//Function to execute the jobs command
void command_jobs()
{
    int i,count=1;
    for(i=0;i<back_count;i++)
    {
	if(back[i].status==1)
	{
	    printf("[%d] %s [%d]\n",count,back[i].name,back[i].pid);
	    count++;
	}
    }
    return;
}
//Function to execute the kjobs command
void command_kjob(char* j,char* s)
{
    int job=atoi(j);
    int sign=atoi(s);
    int i,count=0;

    for(i=0;i<back_count;i++)
    {
	if(back[i].status==1)
	{ 
	    count++;

	    if(count==job)
	    {    
		int a=kill(back[i].pid,sign);
		if(a!=0)
		    return;
		else
		    back[i].status=0;

		break;
	    }
	}
    }
    return;
}
//Function to execute the fg command
void command_fg(char *j)
{
    int job=atoi(j);
    job--;
    int i;
    pid_t t;
    int count=0;
    for(i=0;i<back_count;i++)
    {
	if(back[i].status==1)
	{
	    if(count==job)
	    		break;
	    count++;
	}
    }
    int stats;
    int ret=waitpid(back[i].pid,&stats,0);
    if(ret==-1)
	perror("waitpid()");
    else
    {
	printf("%s with pid %d exited normally\n",back[i].name,back[i].pid);
	back[i].status=0;
    }
    return;
}

//Function to execute the pinfo command
void command_pinfo_1(pid_t u,int flag)
{
    char name[100];
    sprintf(name,"/proc/%d/stat",u);
    int in=open(name,O_RDONLY);
    int i=0;
    char c,buffer[1000];
    while(read(in,&c,1)!=0)
    {
	buffer[i++]=c;
    }
    buffer[i]='\0';

    close(in);
    char *pieces ,*ar[1000];
    int count=0;

    pieces=strtok(buffer," ");
    while(pieces!=NULL)
    {
	pieces[strlen(pieces)]='\0';
	ar[count++]=pieces;
	if(count==1)
	    printf("PID : %s\n",ar[count-1]);
	else if(count==3)
	{
	    printf("Process Status : %s\n",ar[count-1]);
	}
	else if( count==23)
	{
	    printf("Virtual Memory : %s\n",ar[count-1]);
	}
	pieces=strtok(NULL," ");
    }
    ar[count++]=pieces;
    sprintf(name,"/proc/%d/exe",u);
    char buffer2[1000],buffer3[1000];
    int dir;

    if(readlink(name,buffer2,1000)>=0)
    {
	strcpy(buffer3,buffer2);
	int len1=strlen(HOME);
	int len2=strlen(buffer3);
	int x;
	if(len2-len1>0)
	{
	    printf("Executable Path : ");
	    for(x=len1;x<len2;x++)
		printf("%c",buffer3[x]);
	    printf("\n");
	}
    }
    else
	perror("readlink()");

    return;
}

//Function to convert char to int 
void command_pinfo_2(char* p)
{
    int len=strlen(p);

    int i;
    int u=0;
    int power=len-1;
    for(i=0;i<len;i++)
    {
	u+=(p[i]-'0')*pow(10,power);
	power--;
    }
    command_pinfo_1(u,1);
    return;
}
//Function to execute the overkill command
void command_overkill()
{
    int i;
    for(i=0;i<back_count;i++)
    {
	if(back[i].status==1)
	{
	    kill(back[i].pid,SIGTERM);
	    back[i].status=0;
	}

    }
    return;
}
//Function to execute the commands
void exec_cmds(char input[],char* arr[],pid_t p,int count,int flag)
{

    if (strcmp(arr[0],"quit")==0)
	exit(0);
    else if(arr[0]==NULL)
	return;
    else if(strcmp(arr[0],"cd")==0)
	command_cd(arr);
    else if(strcmp(arr[0],"jobs")==0)
	command_jobs();
    else if(strcmp(arr[0],"kjob")==0)
	command_kjob(arr[1],arr[2]);
    else if(strcmp(arr[0],"fg")==0)
	command_fg(arr[1]);
    else if((strcmp(arr[0],"pinfo")==0 ) && (arr[1]==NULL))
	command_pinfo_1(p,0);
    else if((strcmp(arr[0],"pinfo")==0 ) && (arr[1]!=NULL))
	command_pinfo_2(arr[1]);
    else if(strcmp(arr[0],"overkill")==0)
	command_overkill();
    else
    {
	if(flag==1)
	    strcat(input," &");
	exec_external(input,arr,flag);
    }
}

//Function to fork and execvp
void exec_external(char *input,char *arr[],int flag)
{
    pid_t p=fork();

    int state;
    if(flag==0)			//indicate foreground process
    {
	if(p<0)
	{
	    perror("fork not executed correctly!!");
	    exit(1);
	}
	else if(p==0)
	{
	    if(execvp(arr[0],arr)<0)
	    {
		perror("invalid command");
		_exit(0);
	    }
	}
	else
	{
	    parent_pid=p;
	    if(waitpid(p,&state,WUNTRACED)<0)
	    {
		perror("waitpid()");
	    }
	    if(WIFSTOPPED(state))		//convert foreground to background
	    {
		strcpy(back[back_count].name,input);
		back[back_count].pid=parent_pid;
		back[back_count++].status=1;
	    }
	    /*		strcpy(all[all_count].name,input);
			all[all_count].pid=p;
			all[all_count++].status=1;
			wait(NULL);
			while(kill(p,0)>0)
			{
			signal(SIGINT,SIG_IGN);
			signal(SIGINT,signal_handler);
			}
	     */
	}
    }
    else if(flag==1)		//indicate background process
    {
	if(p<0)
	{
	    perror("unable to fork");
	    exit(1);
	}
	else if (p==0)
	{
	    //	    printf("here\n");
	    //printf("New:%s\n",arr[0]);
	    if(execvp(arr[0],arr)<0)
	    {
		perror("maybe an in-built command");
		_exit(0);
	    }
	}
	else
	{
	    //	    printf("there\n");
	    strcpy(back[back_count].name,input);
	    back[back_count].pid=p;
	    back[back_count++].status=1;
	}
    }
}
void signal_handler(int signum)
{
    if(signum==2 || signum==20 || signum ==3)
    {
	if(signum==20)
	{
	    kill(parent_pid,SIGTSTP);
	}
	fflush(stdout);
	printf("\n");
	print_cmd_line();
	fflush(stdout);
	signal(SIGINT, signal_handler);
	signal(SIGQUIT, signal_handler);
	signal(SIGTSTP,signal_handler);
	/*	strcpy(back[back_count].name,all[all_count-1].name);
		back[back_count].pid=all[all_count-1].pid;
		back[back_count++].status=1;
		main();
		}
	 */  }
	return;
	}

void child_handler(int signum)
{
    int p,i=0,count=0;
    p = waitpid(WAIT_ANY, NULL, WNOHANG);
    for(i=0;i<back_count;i++)
    {
	if(back[i].pid==p)
	{
	    int j=0;
	    char temp[100];
	    for(j=0;back[i].name[j]!='&';j++)
	    {
		temp[count++]=back[i].name[j];
	    }
	    temp[count]='\0';
	    fflush(stdout);
	    printf("\n%s with pid %d exited normally\n",temp,back[i].pid);
	    print_cmd_line();
	    fflush(stdout);
	    back[i].status=0;

	}
    }
    signal(SIGCHLD, child_handler);
    return;
}int redirect_parse(const char *c,char input[], char *file[])
{
    char *token;
    int count=0;
    token=strtok(input,c);
    while(token!=NULL)
    {
	token[strlen(token)]='\0';
	file[count]=token;
	count++;
	token=strtok(NULL,c);
    }
    file[count++]=token;
    /*    int i;
	  printf("file : ");
	  for(i=0;file[i]!='\0';i++)
	  printf("%s ",file[i]);
	  printf("\n");
     */    return count;
}
//Function to handle only redirection
void redirect_input_output(char *input)
{
    int stdin_copy,stdout_copy;
    stdin_copy=dup(STDIN_FILENO);		//saving stdin, stdout
    stdout_copy=dup(STDOUT_FILENO);
    int out=0,in=0,argc=0;
    char *right[1000],*argv[1000],*left[1000];
    const char c1[2]=">";

    out=redirect_parse(c1,input,right);

    /*int i;
      for(i=0;right[i]!='\0';i++)
      printf("%s ",right[i]);
      printf("\n");
     */
    const char c2[2]="<";
    in=redirect_parse(c2,right[0],left);
    /*
       for(i=0;left[i]!='\0';i++)
       printf("%s ",left[i]);
       printf("\n");
     */
    const char c3[2]=" ";
    argc=redirect_parse(c3,left[0],argv);
    /*
       for(i=0;argv[i]!='\0';i++)
       printf("%s ",argv[i]);
       printf("\n");
     */


    if(out>2 && in==2)		//output redirection
    {
	//	printf("here\n");
	pid_t p;
	int outf;
	right[1]=strtok(right[1]," ");
	if((outf=creat(right[1], O_WRONLY | S_IRWXU))<0)
	{
	    perror("open()");
	    exit(1);
	}
	else
	{
	    p=fork();
	    if(p<0)
	    {
		perror("unable to fork");
		exit(1);
	    }
	    else if (p==0)
	    {
		dup2(outf,STDOUT_FILENO);		//command ahs to write input to outf
		if(execvp(argv[0],argv)<0)
		{
		    perror("maybe an in-built command");
		    exit(1);
		}
	    }
	    else
		waitpid(p,NULL,0);
	    close(outf);
	}

    }
    else if(in>2 && out==2)		//input redirection
    {
	left[1]=strtok(left[1]," ");
	pid_t p;
	int inf;
	if((inf=open(left[1],O_RDONLY))<0)
	{
	    perror("open()");
	    exit(1);
	}
	else
	{
	    p=fork();

	    if(p<0)
	    {
		perror("unable to fork");
		exit(1);
	    }
	    else if (p==0)
	    {
		dup2(inf,STDIN_FILENO);			//command has to read input from inf
		if(execvp(argv[0],argv)<0)
		{
		    perror("maybe an in-built command");
		    exit(1);
		}
	    }
	    else
		waitpid(p,NULL,0);
	    close(inf);

	}
    }
    else					//both input and output redirection
    {
	pid_t p;
	int outf,inf;
	right[1]=strtok(right[1]," ");
	left[1]=strtok(left[1]," ");
	outf=open(right[1], O_CREAT | O_WRONLY, S_IRWXU);
	inf=open(left[1], O_RDONLY);

	if(outf < 0) 
	{
	    perror(right[1]);
	    exit(1);
	}
	if(inf < 0)
	{
	    perror(left[1]);
	    exit(1);
	}
	p = fork();
	if(p<0)
	{
	    perror("unable to fork");
	    exit(1);
	}
	else if (p==0) 
	{ 
	    dup2(inf,STDIN_FILENO); 		//command has to read input from inf
	    dup2(outf, STDOUT_FILENO); 		//command has to write output to outf
	    if (execvp(argv[0],argv) < 0) 
	    {
		perror("execvp");
		exit(1);
	    }
	}
	else
	    waitpid(p,NULL,0);
	close(inf);
	close(outf);
    }
    dup2(stdin_copy, 0); 			//changing the stdout,stdin back to original
    dup2(stdout_copy, 1);
    close(stdin_copy);
    close(stdout_copy);
    return;
}
//Fubction to handle multiple pipes
void pipe_handling(char input[])
{
    char *pipe_arg[1000],*argv[1000],*ARGV[1000];
    int pcount=0,i,j,in_flag=0,out_flag=0;
    int f_in=-1;					//to indicate last command or not
    int f_out;						//indicate what is the new stdin ie some command's output or stdin

    int stdin_copy,stdout_copy;
    stdin_copy=dup(STDIN_FILENO);
    stdout_copy=dup(STDOUT_FILENO);

    const char c[2]="|";
    pcount=redirect_parse(c,input,pipe_arg);
    pcount--;

    for(i=0;i<pcount;i++)				//loop to execute each pipe_arg
    {
	in_flag=0;					//indicates presence of '<' ie input redirection
	out_flag=0;					//indicate presence of '>' ie output redirection

	//Parsing
	for(j=0;pipe_arg[i][j]!='\0';j++)
	{
	    if(pipe_arg[i][j]=='<')
		in_flag=1;

	    else if(pipe_arg[i][j]=='>')
		out_flag=1;
	}
	int argc=0,ARGC=0;

	if(in_flag==1)
	{
	    const char c1[2]="<";
	    argc=redirect_parse(c1,pipe_arg[i],argv);
	    const char c2[2]=" ";
	    ARGC=redirect_parse(c2,argv[0],ARGV);
	}
	else if(out_flag==1)
	{
	    const char c1[2]=">";
	    argc=redirect_parse(c1,pipe_arg[i],argv);
	    const char c2[2]=" ";
	    ARGC=redirect_parse(c2,argv[0],ARGV);

	}
	else
	{
	    const char c[2]=" ";
	    ARGC=redirect_parse(c,pipe_arg[i],ARGV);
	}
	//ARGV has the actual coomand to be executed
	int pip[2];
	if(i<pcount-1)			//no of pipes needed are pipe_args - 1
	{
	    pipe(pip);
	    f_out=pip[1];		//write end of pipe is stored in f_out
	}
	else
	    f_out=-1;			//indictes last command so write end in stdout

	//pipe + output redirection
	if(out_flag==1)		
	{
	    pid_t p1=fork();
	    if(p1==0)
	    {
		dup2(pip[0],0);					//read end of pipe is the new stdin
		argv[1]=strtok(argv[1]," ");
		int outf=creat(argv[1],O_WRONLY | S_IRWXU);
		if(outf<0)
		{
		    perror("open()");
		    exit(1);
		}
		else
		{
		    p1=fork();
		    if(p1<0)
		    {
			perror("unable to fork");
			exit(1);
		    }
		    else if (p1==0)
		    {
			dup2(outf,STDOUT_FILENO);		//srdout is changed to outf
			if(execvp(ARGV[0],ARGV)<0)		//executing redirection
			{
			    perror("maybe an in-built command");
			    exit(1);
			}
			dup2(stdout_copy, 1);			//stdout is restored 
			close(outf);
		    }
		    else
			wait(NULL);				//child terminates
		    exit(0);					//exit the redirection fork process
		}
	    }
	    else
		wait(NULL);
	}
	//pipe + input redirection
	else if(in_flag==1)
	{
	    pid_t p1=fork();
	    if(p1==0)
	    {
		dup2(pip[1],1);					//write end of pipe is the new stdout
		argv[1]=strtok(argv[1]," ");
		int inf=open(argv[1],O_RDONLY);
		if(inf<0)
		{
		    perror("open()");
		    exit(1);
		}
		else
		{
		    p1=fork();

		    if(p1<0)
		    {
			perror("unable to fork");
			exit(1);
		    }
		    else if (p1==0)
		    {
			dup2(inf,STDIN_FILENO);			//inf is the new stdin
			if(execvp(ARGV[0],ARGV)<0)
			{
			    perror("maybe an in-built command");
			    exit(1);
			}
			dup2(stdin_copy, 0);			//stdin restored
			close(inf);
		    }
		    else
			wait(NULL);				//child terminates
		    exit(0);					//redirection fork process exited
		}
	    }
	    else
		wait(NULL);
	}
	else
	{
	    pid_t p1=fork();
	    if(p1==0)
	    {
	//	if (f_in != -1 && f_in != 0) 
	//for first and last commands
		if(i==0 || i==pcount-1)
		{
	    	dup2(f_in, 0);
	    	close(f_in);
		}
//		if (f_out != -1 && f_in != 1) 			//for !(first) and !(last) commands
		else if(i<pcount-2)
		{
	    	dup2(f_out, 1);
	    	close(f_out);
		}
		if(execvp(ARGV[0],ARGV)<0)
		{
		    perror("execvp()");
		    exit(1);
		}
	    }
	    else
		wait(NULL);
	}
	close(f_in);						//closing f_in nd f_out and assigning new values
	close(f_out);
	f_in=pip[0];						//the new read port is pipe's read port
    }
	return;
}