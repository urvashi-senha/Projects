#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#define MAX 100
int count;
struct node {
	int data;
	struct node* next;
};
typedef struct node node;
struct hash {
	int size;
	node **tbl;
};

struct timespec diff(struct timespec start,struct timespec end)
		{ struct timespec temp;
		  if(end.tv_nsec-start.tv_nsec<0)
		  {  temp.tv_sec=end.tv_sec-start.tv_sec-1;
		     temp.tv_nsec=1000000000+end.tv_nsec-start.tv_nsec;
		  }
		  else
		  { temp.tv_sec=end.tv_sec-start.tv_sec;
		    temp.tv_nsec=end.tv_nsec-start.tv_nsec;
		  }
		  return temp;
	        }  
		  
typedef struct hash hash;
hash* head1=NULL;
hash* head2=NULL;
int f1(int data,hash* head)
{
	return data%head->size;
}
int f2(int data,hash* head)
{
	return (data/head->size)%head->size;
}
void inserth2(int data,int count);
void inserth1(int data,int count)
{
	if(count<MAX)
	{
		int d;
		d=f1(data,head1);
		if(head1->tbl[d]==NULL)
		{
			head1->tbl[d]=(node*)malloc(sizeof(node));
			(head1->tbl[d])->data=data;
			printf("Inserting in first table at %d\n",d);
		}
		else
		{
			int x=(head1->tbl[d])->data;
			printf("Inserting in first table at %d and displacing %d\n",d,x);
			(head1->tbl[d])->data=data;
			count++;
			inserth2(x,count);
		}
	}
	else
	{
		printf("MAX loop limit reached\n");
		return;
	}
}
void inserth2(int data,int count)
{
	int max;
	if(count<MAX)
	{
		int d;
		d=f2(data,head2);
		if(head2->tbl[d]==NULL)
		{
			head2->tbl[d]=(node*)malloc(sizeof(node));
			(head2->tbl[d])->data=data;
			printf("Inserting in second table at %d\n",d);
		}
		else
		{
			int x=(head2->tbl[d])->data;
			printf("Inserting in second table at %d and displacing %d\n",d,x);
			(head2->tbl[d])->data=data;
			count++;
			inserth1(x,count);
		}
	}
	else
	{
		printf("Maximum loop limit reached\n");
		return;
	}
}
void lookup(int x)
{
	int func1=f1(x,head1);
	int func2=f2(x,head2);
	if(head1->tbl[func1]==NULL)
		printf("NOT FOUND\n");
	else if(head1->tbl[func1]->data==x)
	{
		printf("Found in first hash table at %d\n", func1);
		return;
	}
	if(head2->tbl[func2]==NULL)
		printf("NOT FOUND\n");
	else if(head2->tbl[func2]->data==x)
	{
		printf("Found in second hash table at %d\n", func2);
		return;
	}
	else
	{
		printf("Not Found\n");
		return;
	}
}

int main()
{       struct timespec begin,end,insert_time,find_time;
	count=0;
	int data;
	int in=0,fi=0;
	int c;
	insert_time.tv_sec=0;
	find_time.tv_sec=0;
	insert_time.tv_nsec=0;
	find_time.tv_nsec=0;
	head1=NULL;
	head2=NULL;
	head1=malloc(sizeof(hash));
	head2=malloc(sizeof(hash));
	head1->size=100001,head2->size=100001;
	getchar();
	head1->tbl=(node**)malloc(sizeof(node*)*(head1->size));
	head2->tbl=(node**)malloc(sizeof(node*)*(head2->size));
	scanf("%d",&c);
	while(c!=3)
	{
		if(c==1)
		{       clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&begin);
			scanf("%d",&data);
                        inserth1(data,count);
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&end);
		//printf("Time insert %ld : %ld \n",diff(begin,end).tv_sec,diff(begin,end).tv_nsec);
			insert_time.tv_nsec+=diff(begin,end).tv_nsec;
			insert_time.tv_sec+=diff(begin,end).tv_sec;
			in++;
		}
		else if(c==2)
		{       clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&begin);
			scanf("%d",&data);
			lookup(data);
			clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&end);
	//		printf("Time find %ld : %ld \n",diff(begin,end).tv_sec,diff(begin,end).tv_nsec);
			find_time.tv_sec+=diff(begin,end).tv_sec;
			find_time.tv_nsec+=diff(begin,end).tv_nsec;
			fi++;

		}
		scanf("%d",&c);
	}
	printf("time to insert %d  elements are %ld : %ld\n",in,insert_time.tv_sec,insert_time.tv_nsec);
	printf("time to find %d elements are %ld : %ld\n",fi,find_time.tv_sec,find_time.tv_nsec);
	return 0;
}






