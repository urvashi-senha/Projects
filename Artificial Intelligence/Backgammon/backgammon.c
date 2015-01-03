#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node
{
    int s;
    int d;
    int u;
    int max;
    int child;
    struct node* next[90];
}node;

typedef node* link;
link root1,root2,move1,move2;

char bar[15];
int A[13]={0},B[13]={0},R1,R2,bar_var1=0,bar_var2=0,board[25]={0},board2[25]={0};

link min_ptr1;
int min_value1=10000;
link min_ptr2;
int min_value2=10000;
int search_flag = 0;

link create_move(int ,int, link ,int,int*);
void game_tree(int *board1,int D1,int D2,link root,int level);
int utility(int x,int y,int* b,int c);
int check_bearing(int *b,int c);
void choose(link root,int level,int order);
void search(link min_ptr,link root, int level);
int bear_utility(int x, int y,int *b,int c);
void print_board(int * bo)
{
    int j;
    for(j=1;j<=24;j++)
	printf("%d ",bo[j]);
    printf("\n");
}

int main()
{
    int i,k,j,l,m,p;
    for(i=1;i<=24;i++)
    {
	scanf("%d",&board[i]);
	board2[i] = board[i];
    }

    scanf("%s",bar);
    int z=0;
    for(z=0;z<strlen(bar);z++)
    {
	if(bar[z]=='e')
	{
	    bar_var1 =0;
	    bar_var2=0;
	    break;
	}
	if(bar[z]=='a')
	    bar_var1++;
	if(bar[z]=='b')
	    bar_var2++;
    }

    scanf("%d%d",&R1,&R2);

    root1 = (link)malloc(sizeof(node));
    root1->s = -100;
    root1->d = -100;
    root1->child =0;
    root1->max = -100;

    root2 = (link)malloc(sizeof(node));
    root2->child =0;
    root2->s = -100;
    root2->d = -100;
    root2->max = -100;

    move1 = (link)malloc(sizeof(node));
    move1->child =0;
    move1 -> s = -100;
    move1 -> d = -100;

    move2 = (link)malloc(sizeof(node));
    move2->child =0;
    move2 -> s = -100;
    move2 -> d = -100;

    k = 1; 

    if(bar_var1 ==0)
    {
	int r, max1=0, max2=0;

	if(check_bearing(board,1))
	{
	    if(move1->d == -100)
	    {
		link array1,array2;
		int max1=0,max2=0,r,i=0;
		array1=(link)malloc(sizeof(node)*6);
		array2=(link)malloc(sizeof(node)*6);

		for(r=16;r<25;r++)
		{
		    array1[i].s=i;
		    array1[i].d=i+R1;
		    array1[i].u=bear_utility( r, r+R1, board,1);
		    if(array1[i].u>array1[max1].u)
			max1=i;
		    array2[i].s=i;
		    array2[i].d=i+R2;
		    array2[i].u=bear_utility(r, r+R2, board,1);
		    if(array2[i].u>array2[max2].u)
			max2=i;
		    i++;
		}
		if(array1[max1].u>array2[max2].u)
		{
		    board[array1[max1].s]--;
		    if(i+R1<25)
			board[array1[max1].d]++;
		    move1->s = array1[max1].s;
		    move1->d = array1[max1].d;
		    max1=0;
		    max2=0;
		for(r=16;r<25;r++)
		{
		    array2[i].s=i;
		    array2[i].d=i+R2;
		    array2[i].u=bear_utility( r, r+R2,board, 1);
		    if(array2[i].u>array2[max1].u)
			max1=i;
		}
		move2->s = array2[max1].s;
		move2->d == array2[max1].d;
		}
		else
		{
		    board[array1[max2].s]--;
		    if(i+R2<25)
			board[array2[max2].d]++;
		    move1->s = array2[max2].s;
		    move1->d = array2[max2].d;
		    max1=0;
		    max2=0;
		for(r=16;r<25;r++)
		{
		    array1[i].s=i;
		    array1[i].d=i+R2;
		    array1[i].u=bear_utility( r, r+R1, board,1);
		    if(array1[i].u>array1[max1].u)
			max1=i;
		}

		    move1->s = array1[max1].s;
		    move1->d = array1[max1].d;

		}

	    }
	}
	else
	{
	game_tree(board,R2,R1,root2,1);
	game_tree(board2,R1,R2,root1,1);
	}
    }
    else if(bar_var1>=1)
    {
	link temp1,temp2;

	temp1 = (link)malloc(sizeof(node));
	temp1->s = 0;
	temp1->d = R1;
	temp1->u = utility(0,R1,board,1);

	temp2 = (link)malloc(sizeof(node));
	temp2->s = 0;
	temp2->d = R2;
	temp2->u = utility(0,R2,board,R2);

	if(bar_var1 == 1)
	{
	    if(temp1->u > temp2->u)
	    {
		if(board[R1]>=-1)
		{
		    move1 -> d = temp1->d;
		    if(board[R1]==-1)
			board[R1]=1;
		    else
			board[R1]++;
		    game_tree(board,R2,R1,root1,2);
		}
	    }
	    if(move1->d == -100)
	    {
		if(board[R2]>=-1)
		{
		    move1->d = temp2->d;
		    if(board[R2]==-1)
			board[R2] = 1;
		    else
			board[R2]++;
		    game_tree(board,R1,R2,root1,2);
		}
	    }
	    if(move1->d == -100)
		printf("pass\npass\n");

	}
	else if(bar_var1>=2)
	{
	    if(temp1->u > temp2->u)
	    {
		print_board(board);
		if(board[R1]>=-1)
		{
		    move1 -> d = temp1->d;
		    if(board[R1]==-1)
			board[R1]=1;
		    else
			board[R1]++;
		}
		if(board[R2]>=-1)
		{
		    move2 -> d = temp2->d;
		}
		if(move1->d == -100 && move2 -> d== -100)
		    printf("pass\npass\n");
		else if(move1->d == -100 && move2->d!=-100)
		    printf("Z %d\npass\n",move2->d);
		else if(move1->d != -100 && move2->d == -100)
		    printf("Z %d\npass\n",move1->d);
		else if(move1->d != -100 && move2->d != -100)
		    printf("Z %d\nZ %d\n",move1->d,move2->d);
	    }
	    else
	    {
		if(board[R2]>=-1)
		{
		    move1->d = temp2->d;
		    if(board[R2]==-1)
			board[R2] = 1;
		    else
			board[R2]++;
		}
		if(board[R1]>=-1)
		{
		    move2->d = temp1->d;
		}
		if(move1->d == -100 && move2 ->d == -100)
		    printf("pass\npass\n");
		else if(move1->d == -100 && move2->d!=-100)
		    printf("Z %d\npass\n",move2->d);
		else if(move1->d != -100 && move2->d == -100)
		    printf("Z %d\npass\n",move1->d);
		else if(move1->d != -100 && move2->d != -100)
		    printf("Z %d\nZ %d\n",move1->d,move2->d);
	    }

	}
    }


    /*for(i=0; i<root1->child; i++)
      {
      printf("s-> %d, d->%d u-> %d\n",root1->next[i]->s, root1->next[i]->d,root1->next[i]->u );
      {
      for(j=0; j<root1->next[i]->child; j++)
      {
      printf("  s-> %d, d->%d u-> %d\n", root1->next[i]->next[j]->s, root1->next[i]->next[j]->d, root1->next[i]->next[j]->u);
      for(k=0;k<root1->next[i]->next[j]->child;k++)
      {	
      printf("     s-> %d, d->%d  u-> %d\n", root1->next[i]->next[j]->next[k]->s, root1->next[i]->next[j]->next[k]->d,root1->next[i]->next[j]->next[k]->u);
      for(m=0;m<root1->next[i]->next[j]->next[k]->child;m++)
      {
      printf("       s-> %d, d->%d  u-> %d\n", root1->next[i]->next[j]->next[k]->next[m]->s, root1->next[i]->next[j]->next[k]->next[m]->d,root1->next[i]->next[j]->next[k]->next[m]->u);
      for(l=0;l<root1->next[i]->next[j]->next[k]->next[m]->child;l++)
      {
      printf("         s-> %d, d->%d  u-> %d\n", root1->next[i]->next[j]->next[k]->next[m]->next[l]->s, root1->next[i]->next[j]->next[k]->next[m]->next[l]->d, root1->next[i]->next[j]->next[k]->next[m]->next[l]->u);
      for(p=0;p<root1->next[i]->next[j]->next[k]->next[m]->next[l]->child;p++)
      {
      printf("           s-> %d, d->%d  u-> %d\n", root1->next[i]->next[j]->next[k]->next[m]->next[l]->next[p]->s, root1->next[i]->next[j]->next[k]->next[m]->next[l]->next[p]->d,root1->next[i]->next[j]->next[k]->next[m]->next[l]->next[p]->u);
      }
      }

      }
      }
      }
      }
      }

      for(i=0; i<root2->child; i++)
      {
      printf("s-> %d, d->%d\n",root2->next[i]->s, root2->next[i]->d );
      {
      for(j=0; j<root2->next[i]->child; j++)
      { printf("  s-> %d, d->%d\n", root2->next[i]->next[j]->s, root2->next[i]->next[j]->d);
      {
      for(k=0;k<root2->next[i]->next[j]->child;k++)
      {
      printf("     s-> %d, d->%d\n", root2->next[i]->next[j]->next[k]->s, root2->next[i]->next[j]->next[k]->d);
      {
      for(m=0; m<root2->next[i]->next[j]->next[k]->child; m++)
      {
      printf("         s->%d, d->%d\n", root2->next[i]->next[j]->next[k]->next[m]->s, root2->next[i]->next[j]->next[k]->next[m]->d);
      for(l=0;l<root2->next[i]->next[j]->next[k]->next[m]->child;l++)
      {
      printf("         s-> %d, d->%d\n", root2->next[i]->next[j]->next[k]->next[m]->next[l]->s, root2->next[i]->next[j]->next[k]->next[m]->next[l]->d);
      for(p=0;p<root2->next[i]->next[j]->next[k]->next[m]->next[l]->child;p++)
      {
      printf("           s-> %d, d->%d\n", root2->next[i]->next[j]->next[k]->next[m]->next[l]->next[p]->s, root2->next[i]->next[j]->next[k]->next[m]->next[l]->next[p]->d);
      }
      }

      }
      }
      }
      }
      }
      }
      }
*/   

    choose(root1,0,0);
    choose(root2,0,1);

   if(min_value1 < min_value2)
   	search(min_ptr1,root1, 0);
   else
   	search(min_ptr2,root2, 0);
if(bar_var1==0)
{
    if(move1->d==-100)
	printf("pass\n");
    else
    printf("%d %d\n",move1->s,move1->d);
    if(move2->d == -100)
	printf("pass\n");
    else
	printf("%d %d\n",move2->s,move2->d);
}   
    return 0;
}

link create_move(int pos,int dice, link head,int c,int *b)
{

    link temp;
    temp = (link)malloc(sizeof(node));
    temp->s = pos;
    temp->d = pos + dice;
    temp->u = utility(pos,pos+dice,b,c);
    temp->max = -100;
    //        printf("pos : %d pos+dice = %d u %d\n",pos,pos+dice,temp->u);
    //       print_board(b);
    temp->child = 0; 

    head->next[head->child] = (link)malloc(sizeof(node)); 
    head -> next[head->child] = temp;
    head->child++;
    head ->next[head->child+1] = NULL;
    return head;

}

void game_tree(int *board1,int D1,int D2,link root, int level)
{
    int i=0,bar_flag=0,j=0,k=0,m=0,n=0,p=0,q=0;
    if(level<=2)
    {  for(i=1;i<=24;i++)
	{
	    if(board1[i]>0)
	    {
		if(board1[i + D1] >= -1 && i+D1<25)
		{
		    root = create_move(i,D1,root,1,board1); 
		    board1[i]--;
		    if(board1[i+D1]==-1)
		    {
			board1[i+D1]=1;
			bar_flag=1;
		    }	
		    else
			board1[i+D1]++;

		    game_tree(board1,D2,D1,root->next[root->child - 1],level+1);

		    if(bar_flag==1)
		    {
			board1[i+D1]=-1;
			board[0] -= 1;
		    }
		    else
			board1[i+D1]--;
		    board1[i]++;

		}
	    }
	}
    }
    else if( level >= 3 && level<=4)
    {
	if(bar_var2==0)
	{
	    for(k=1;k<=6;k++)
	    {
		if(k!=D1)
		{
		    for(j=1;j<=24;j++)
		    {
			if(board1[j] <= -1)
			{
			    if(board1[j+k] <= 1 && j + k < 25)
			    {
				root = create_move(j,k,root,2,board1);
				board1[j] ++;
				if(board1[j+k]==1)
				{
				    bar_flag = 1;
				    board1[j+k] = -1;
				}
				else
				    board[j+k] --;

				game_tree(board1,k,k,root->next[root->child-1],level+1);
				if(bar_flag==1)
				    board1[j+k]= 1;
				else
				    board1[j+k]++;
				board1[j]--;


			    }
			}
		    }
		}
	    }
	}
    }
    else if(level==5 || level==6)
    {
	for(m=1;m<=6;m++)
	{
	    if(m!=D1)
	    {
		for(n=1;n<=24;n++)
		{
		    if(board1[n]>0)
		    {
			if(board1[n+m]>=-1 && m+n<25)
			{
			    root = create_move(n,m,root,1,board1);

			    board1[n]--;
			    if(board1[n+m]==-1)
			    {
				board1[n+m]=1;
				bar_flag=1;
			    }	
			    else
				board1[n+m]++;

			    game_tree(board1,m,m,root->next[root->child - 1],level+1);

			    if(bar_flag==1)
				board1[n+m]=-1;
			    else
				board1[n+m]--;
			    board1[n]++;
			}
		    } 
		}
	    }
	}

    }
    else if(level == 7 && level ==8)
    {
	if(bar_var2==0)
	{
	    for(p=1;p<=6;p++)
	    {
		if(p!=D1)
		{
		    for(q=1;q<=24;q++)
		    {
			if(board1[q] <= -1)
			{
			    if(board1[q+p] <= 1 && q + p < 25)
			    {
				root = create_move(q,p,root,2,board1);
				board1[q] ++;
				if(board1[q+p]==1)
				{
				    bar_flag = 1;
				    board1[q+p] = -1;
				}
				else
				    board[q+p] --;

				game_tree(board1,p,p,root->next[root->child-1],level+1);
				if(bar_flag==1)
				    board1[q+p]= 1;
				else
				    board1[q+p]++;
				board1[q]--;


			    }
			}
		    }
		}
	    }
	}
    }
    return;
}
int utility(int x,int y,int* b,int c)
{
    int u =5;
    int i;
    int temp;
    if(c==1)		//white is moving
	i=18;
    else if(c==2)	//black is moving
	i=1;

    for(;i<25; i++)
    {
	if(c==1 && b[i]>0)
	    temp+=b[i];
	else if(c==2 && b[i]<0)
	{
	    temp+=(-1)*b[i];
	    if(i==6)
		break;
	}
    }
    if((temp<=3 && c==1 && y>=16)||(temp<=3 && c==2 && y<=6))
	u+=10;
    if(((y==4||y==5||y==7)&&c==1)||((y==20||y==21||y==22)&&c==2))
	u+=5;
    if(b[y]==5)
	u+=5;
    if(((c==1)&&(y==20||y==21))||((c==2)&&(y==4||y==5)))
	u+=5;
    if((c==1&&y<=6)||(c==2&&y>=18))
	u+=5;
    if((b[y]==-1&&c==1)||(b[y]==1&&c==2))
	u+=2;
    if((c==1&&b[x]==2&&b[y]==-1)||(c==2&&b[x]==-2&&b[y]==1))
	u-=5;
    if((c==1&&(b[x]>=3 || b[x]==1) &&b[y]==-1)||(c==2&&(b[x]==-1|| b[x]<=-3) && b[y]==1))
	u+=10;
    if(b[y]==6)
	u-=5;
    if((c==1&&b[x]==2&&b[y]==0)||(c==2&&b[x]==-2&&b[y]==0))
	u-=5;
    return u; 


}
int bear_utility(int x, int y,int *b,int c)
{
    int u = 5;

    if((c==1&&b[y]==1)||(c==2&&b[y]==-1))
	u+=15;
    if((c==1&&b[x]==1)||(c==2&&b[x]==-1))
	u+=15;
    if((c==1&&b[x]>=15/6&&b[y]<=15/6)||(c==2&&b[x]<=-15/6&&b[y]>=-15/6))
	u+=15;
    if((c==1&&y>25&&b[x]>2)||(c==2&&y>25&&b[x]<-2))
	u+=20;
    if((c==1&&b[x]==2&&y>25)||(c==2&&b[x]==-2&&y>25))
	u-=10;
    if((c==1&&b[x]>=6)||(c==2&&b[x]<=-6))
	u-=5;
    else if(y>25)
	u+=20;
}

int check_bearing(int *b,int c)
{
    int count=0,a;

    if(c==1)
    {
	for(a=1;a<=17;a++)
	{
	    if(b[a]>0)
		return 0;
	}
	return 1;
    }

}

link parent;



void search(link min_ptr,link root, int level)
{
    int i;

    if(root != min_ptr)
    {
	for(i=0; i<root->child; i++)
	{
	    if(search_flag == 0)
		search(min_ptr,root->next[i], level+1);
	}
    }

    else
    {
	search_flag = 1;
    }

    if(search_flag == 1 && level==2)
    {
	move2->s = root->s;
	move2->d = root->d;
    }

    if(search_flag == 1 && level==1)
    {
	move1->s = root->s;
	move1->d = root->d;
    }
}


void choose(link root,int level,int order)
{
    int i,j,k,l;
    if(level==7 || level<=5)
    {
	for(i=0;i<root->child;i++)
	    choose(root->next[i],level+1,order);
    }
    else if(level == 6)
    {
	parent = root;
	parent -> max = -100;

	for(j=0;j<parent->child;j++)
	{
	    choose(parent->next[j],level+1,order);
	    //	    if(grandparent -> max > root->max )
	    //		grandparent -> max = root->max;
	}

	if(order==0 && root->max < min_value1)
	{
	    min_value1 = root->max;
	    min_ptr1 = root;
	}
	if(order==1 && root->max < min_value2)
	{
	    min_value2 = root->max;
	    min_ptr2 = root;
	}

    }
    else if(level == 8)
    {
	if(root->u > parent -> max)
	    parent -> max = root -> max;
    }
}
