#include<stdio.h>
#include<stdlib.h>
struct node
{
	int info;
	struct node *left, *right;
};
struct node* list = NULL;
void insertnode(int pos, int val) 
{
	struct node* ins = (struct node*) malloc(sizeof(struct node));
	ins->info = val;
	ins->left = NULL;
	ins->right = NULL;
	if(pos == 1)
	{
		ins->right = list;
		list = ins;
		struct node *succ = ins->right;
		if(succ != NULL)
			succ->left = ins;
	}
	else
	{
		struct node *pred = list;
		for(int i = 1; i < pos - 1; i++)
			pred = pred->right;
	    ins->right = pred->right;
	    pred->right = ins;
	    struct node *succ = ins->right;
		if(succ != NULL)
	    	succ->left = ins;
	    ins->left = pred;
	}	
}
void deletenode(int pos)
{
	struct node *del = list;
	if(pos == 1) 
	{
		struct node *succ = del->right;
		list  = succ;		
		if(succ != NULL)
			succ->left = NULL;
	}
	else
	{
		for(int i = 1; i < pos; i++)
			del = del->right;
		struct node *pred = del->left;
		pred->right = del->right;
		struct node *succ = del->right;
		if(succ != NULL)
			succ->left = pred;
	}
	free(del);
}
void display() 
{
	struct node* temp = list;
	while(temp != NULL) 
	{
      	printf("%d\t", temp->info);
      	temp = temp->right;
   	}
   	printf("\n");
}
void search(int val) 
{
	struct node* temp = list;
	while(temp != NULL) 
	{
      	if(temp->info == val)
      	{
			printf("Found\n");
			break;
		}
      	temp = temp->right;
   	}
   	if(temp == NULL)
   		printf("Not found\n");
}
int main()
{
	int choice, pos, val;
	while(1)
	{
		printf("-------Menu------\n");
		printf("1. Insert\n");
		printf("2. Delete\n");
		printf("3. Display\n");
		printf("4. Search\n");
		printf("5. Clear\n");
		printf("6. Exit\n");
		printf("Enter a choice (1-6):");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				printf("Enter position to insert:");
				scanf("%d", &pos);
				printf("Enter value to insert:");
				scanf("%d", &val);
				insertnode(pos, val);
				break;
			case 2:
				printf("Enter position to delete:");
				scanf("%d", &pos);
				deletenode(pos);
				break;
			case 3:
				display();
				break;
			case 4:
				printf("Enter value to search:");
				scanf("%d", &val);
				search(val);
				break;
			case 5:
				system("clear");
				break;
			case 6:
				exit(0);
			default:
				printf("Wrong choice!\n");
		}
	}	
}