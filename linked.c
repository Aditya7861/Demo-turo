// data 8 Aug 18 
#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    struct node *link;
};
struct node *start=NULL;
struct node* createNode()
{
    struct node *n;
    n = (struct node *)malloc(sizeof(struct node *));
    return n;
}
void insertNode()
{
    struct node * temp,*t;
    temp=createNode();
    printf("Enter a Numner");
    scanf("%d",&temp->info);
    temp->link=NULL;
    if(start==NULL)
        start=temp;
    else
    {
        t=start;
        while(t->link!=NULL)
        {
            t=t->link;
        }
        t->link=temp;
    }
}
void deleteNode()
{
    struct node *r;
    if(start==NULL)
        printf("List is Empty");
    else
    {
        r=start;
        start=start->link;
        free(r);
    }
} 
void view_node()
{
    struct node * t;
    if(start==NULL)
        printf("List empty");
    else{
        t=start;
        while(t!=NULL)
        {
            printf("%d",t->info);
            t=t->link;
        }
    }

}
int menu()
{
    int ch;
    printf("1.Insert Node:- \n 2.Delete Node:- \n 3.View Node:- \n 4.Exit :-");
    scanf("%d",&ch);
    return ch;
}
void main()
{
    while(1)
    {
        switch(menu())
        {
            case 1:insertNode();
                   break;
            case 2:deleteNode();
                   break;
            case 3:view_node();
                   break;
            case 4:exit(0);
                   break;
            defalut:printf("Please Try again");
        }
    }
}
