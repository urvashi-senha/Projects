#include<stdio.h>
#include<time.h>
typedef struct function
{
	int a;
	int b;
}function;

int table[1000001]={0};
function array[20];

void insert(int no,int i)
{
	int index=(array[i].a*no+array[i].b)%1000000;
	int j;
		//printf(" : %d index : %d\n",no,index);
	if(table[index]==0)
	{
		table[index]=no;
	}
	else
	{
		int p=index;
		while(index<999999 && table[index]!=0)
			index++;
		if(index==999999)
		{
			for(j=0;j<p;j++)
			{
				if(table[index]==0)
				{
					table[index]=no;
					break;
				}
			}
			if(i==p)
				printf("Cannot insert into the hash\n");
		}
	}

}

void find(int no,int i)
{
	int flag=0;int j;
	int index=(array[i].a*no+array[i].b)%1000000;

	if(table[index]==no)
	{
		printf("Present1\n");
	}
	else
	{
		int p=index;
		while(index<999999 && table[index]!=no)
			index++;
//		printf("index:%d\n",index);
		if(index==999999)
		{
			for(j=0;j<p;j++)
			{
				if(table[j]==no)
				{
					printf("Present2\n");
					break;
				}
			}
			if(j==p)
				printf("Not Present\n");
		}
		else
			printf("Present3\n");
	}
}

struct timespec diff(struct timespec start,struct timespec end)
{
	struct timespec temp;
	if(end.tv_nsec-start.tv_nsec<0)
	{
		temp.tv_sec=end.tv_sec-start.tv_sec-1;
		temp.tv_nsec=1000000000+end.tv_nsec-start.tv_nsec;
	}
	else
	{
		temp.tv_sec=end.tv_sec-start.tv_sec;
		temp.tv_nsec=end.tv_nsec-start.tv_nsec;
	}
	return temp;
}

int main()
{
	struct timespec begin,end,insert_time,find_time;
	int i;
	for(i=0;i<20;i++)
	{
		array[i].a=rand()%10000;
		array[i].b=rand()%10000;
	}
	int function_no=rand()%20;
	insert_time.tv_sec=0;
	find_time.tv_sec=0;
	insert_time.tv_nsec=0;
	find_time.tv_nsec=0;

	printf("%d %d\n",array[function_no].a,array[function_no].b);
	int d,c;
	printf("1-insertion 2-search 3-quit\n");
	scanf("%d",&c);
	int in=0,fi=0;
	while(1)
	{
		if(c==1)
		{
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&begin);
			scanf("%d",&d);
			insert(d,function_no);
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&end);
			//xi[in++]=d;
		//	printf("Time to insert %d %ld : %ld \n",d,diff(begin,end).tv_sec,diff(begin,end).tv_nsec);
		//	ti[in++]=diff(begin,end).tv_sec,diff(begin,end).tv_nsec;
			insert_time.tv_sec+=diff(begin,end).tv_sec;
			insert_time.tv_nsec+=diff(begin,end).tv_nsec;
			in++;

		}
		else if(c==2)
		{
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&begin);
			scanf("%d",&d);
			find(d,function_no);
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&end);
			//xf[fi++]=d;
			//printf("Time to find %d  %ld: %ld \n",d,diff(begin,end).tv_sec,diff(begin,end).tv_nsec);
			find_time.tv_sec+=diff(begin,end).tv_sec;
			find_time.tv_nsec+=diff(begin,end).tv_nsec;
			fi++;
		}
		else if(c==3)
			break;
		scanf("%d",&c);
	}
	printf("Time to insert  %d elements are %ld:%ld\n",in,insert_time.tv_sec,insert_time.tv_nsec);
	printf("Time to find %d elements are  %ld:%ld\n",fi,find_time.tv_sec,find_time.tv_nsec);
	return 0;
}
