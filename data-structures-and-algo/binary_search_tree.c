#include <stdio.h>
#include <stdlib.h>
struct node
{
	int info;
	struct node *left, *right;
};
struct node *root = NULL;
struct node *search(int val) 
{
	struct node *curr = root;
	for(;;)
	{
		if(curr == NULL)
			return NULL;
		if(val == curr->info)
			return curr;
		else if(val < curr->info)
			curr = curr->left;
		else
			curr = curr->right;
	}
}
void insert(int val) 
{
	struct node *ins = (struct node*) malloc(sizeof(struct node));
	ins->info = val;
	ins->left = NULL;
	ins->right = NULL;
	if(root == NULL)
		root = ins;
	else
	{
		struct node *parent = NULL, *curr = root;
		while(curr != NULL)
		{
			parent = curr;
			if(ins->info < curr->info)
				curr = curr->left;
			else if(ins->info > curr->info)
				curr = curr->right;	
			else
				return;				
		}
		if(ins->info < parent->info)
			parent->left = ins;
		else
			parent->right = ins;		
	}
}
void del(int val) 
{
	struct node *parent = NULL, *curr = root;
	while(curr->info != val)
	{
		parent = curr;
		if(val < curr->info)
			curr = curr->left;
		else
			curr = curr->right;					
	}
	if(curr->left == NULL && curr->right == NULL)
	{
		if(parent == NULL)
		{
			root = NULL;
			free(curr);
		}
		else
		{
			if(curr->info < parent->info)
				parent->left = NULL;
			else
				parent->right = NULL;
			free(curr);
		}
	}
	else if(curr->left == NULL && curr->right != NULL)
	{
		if(parent == NULL)
		{
			root = curr->right;
			free(curr);
		}
		else
		{
			if(curr->info < parent->info)
				parent->left = curr->right;
			else
				parent->right = curr->right;
			free(curr);
		}		
	}
	else if(curr->left != NULL && curr->right == NULL)
	{
		if(parent == NULL)
		{
			root = curr->left;
			free(curr);
		}
		else
		{
			if(curr->info < parent->info)
				parent->left = curr->left;
			else
				parent->right = curr->left;
			free(curr);
		}		
	}
	else
	{
		struct node *leftmost = curr->right, *pre = curr;
		while(leftmost->left != NULL)
		{
			pre = leftmost;
			leftmost = leftmost->left;			
		}
		curr->info = leftmost->info;
		if(leftmost->info < pre->info)
			pre->left = leftmost->right;
		else
			pre->right = leftmost->right;
		free(leftmost);
	}		
}
void preorder(struct node *n) 
{
	if (n != NULL)
	{		
		printf("%d ", n->info);
		preorder(n->left);
    	preorder(n->right);
  	}
}
void inorder(struct node *n) 
{
	if (n != NULL)
	{
		inorder(n->left);
		printf("%d ", n->info);
    	inorder(n->right);
  	}
}
void postorder(struct node *n) 
{
	if (n != NULL)
	{
		postorder(n->left);		
    	postorder(n->right);
    	printf("%d ", n->info);
  	}
}
int main()
{
	int c, n;
	while(1)
	{
		printf("1. Insert\n");
		printf("2. Delete\n");
		printf("3. Search\n");
		printf("4. Preorder Traversal\n");
		printf("5. Inorder Traversal\n");
		printf("6. Postorder Traversal\n");
		printf("7. Clear\n");
		printf("8. Exit\n");
		printf("Enter choice:");
		scanf("%d", &c);
		switch(c)
		{
			case 1:
				printf("Enter value to insert:");
				scanf("%d", &n);
				insert(n);
				break;
			case 2:
				printf("Enter value to delete:");
				scanf("%d", &n);
				del(n);
				break;
			case 3:
				printf("Enter value to serach:");
				scanf("%d", &n);
				if(search(n) == NULL)
					printf("Not found\n");
				else
					printf("Found\n");
				break;
			case 4:
				printf("Preorder traversalis:");
				preorder(root);
				printf("\n");
				break;
			case 5:	
				printf("Inorder traversal:");
				inorder(root);
				printf("\n");
				break;
			case 6:	
				printf("Postorder traversal:");
				postorder(root);
				printf("\n");
				break;
			case 7:
				system("CLS");
				break;
			case 8:
				exit(0);
			default:
				printf("Wrong choice!\n");
		}		
	}	
}