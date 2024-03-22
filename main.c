//The File Created By Mohammad Hosein Mohseni(402149059) And Mahdi Karimi(402149058).
//Master: Fatemeh Porgholamali
//Valiasr Rafsanjan University
//Computer Engineering 1402
//Term: 4021
#include <stdio.h>

// Function For print Random Maze at the moment.
void PM(int row,int col,char mat[row][col]){
    for(int i=0;i<row;i++){
        for (int j = 0; j < col ; j++) {
            printf("%c  ",mat[i][j]);
        }
        printf("\n");
    }
}

// Function for Generating Random Maze.
void Random_Maze_Generator(int isp,int jsp,int row_size,int col_size,char mat[row_size][col_size], FILE *file)
{
    int ii, jj, i=isp, j=jsp, rep, k;
    char dir, temp;

    //Fill Maze with Walls(#)
    for(ii=0;ii<row_size;ii++){
        for (jj = 0; jj < col_size ; jj++) {
            mat[ii][jj]='#';
        }
    }

    //Defining Entrance
    mat[i][j]='.';

    if(i==0){
        i++;
        mat[i][j]='.';
    }
    else if(i==row_size-1){
        i--;
        mat[i][j]='.';
    }
    else if(j==0){
        j++;
        mat[i][j] = '.';
    }
    else if(j==col_size-1){
        j--;
        mat[i][j]='.';
    }
    PM(row_size,col_size,mat);

    //Loop for Movement
    while(j>0 && j<col_size-1 && i>0 && i<row_size-1){
        printf("Enter Reputation(1 2 3 ...) AND Direction(U D R L): \n");
        scanf("%c",&temp); // for \n

        scanf("%d %c", &rep, &dir);

        //Error Control
        if(rep<=0){
            printf("Error: Wrong Reputation! Try Again: \n");
            continue;
        }


        //Conditions for Movement in specific Direction
        if (dir == 'U' || dir == 'u') { //Move Up
            if(rep>i){// Error Control
                printf("Error: Extra Reputation on Up! Try Again: \n");
                continue;
            }
            for (k=0;k<rep;k++) {
                mat[i][j]='.';
                i--;
                mat[i][j] = '0';
            }
            PM(row_size, col_size, mat);
        }
        else if (dir == 'D' || dir == 'd') { //Move Down
            if(i+rep>row_size-1){// Error Control
                printf("Error: Extra Reputation on Down! Try Again: \n");
                continue;
            }
            for (k=0;k<rep;k++) {
                mat[i][j]='.';
                i++;
                mat[i][j] = '0';
            }
            PM(row_size, col_size, mat);
        }
        else if (dir == 'R' || dir == 'r') {//Move Right
            if(j+rep>col_size-1){// Error Control
                printf("Error: Extra Reputation on Right! Try Again: \n");
                continue;
            }
            for(k=0;k<rep;k++) {
                mat[i][j]='.';
                j++;
                mat[i][j] = '0';
            }
            PM(row_size, col_size, mat);
        }
        else if (dir == 'L' || dir == 'l') { //Move Left
            if(rep>j){// Error Control
                printf("Error: Extra Reputation on Left! Try Again: \n");
                continue;
            }

            for(k=0;k<rep;k++) {
                mat[i][j]='.';
                j--;
                mat[i][j] = '0';
            }
            PM(row_size, col_size, mat);
        }
        else{
            printf("Error: Wrong Direction Input! Try Again: \n");
            continue;
        }

    }

    //Change '0' Cursor to '.'
    for (int x = 0; x < row_size; x++) {
        for (int y = 0; y < col_size; y++) {
            if (mat[x][y] == '0') mat[x][y] = '.';
        }
    }

    // Writing Generated matrix in file.
    for(ii=0;ii<row_size;ii++){
        for(jj=0;jj<col_size;jj++){
            fprintf(file,"%c",mat[ii][jj]);
        }
        fprintf(file,"\n");
    }
}

// Function for reading File and convert it to Matrix.
void File_to_Matrix(FILE* file,int row_size,int column_size,char matrix[row_size][column_size])
{
    char CH;
    for(int i=0;i<row_size;i++){
        for(int j=0;j<column_size;j++){
            CH= (char)fgetc(file);
            matrix[i][j]=CH;
        }
        fgetc(file);
    }
}

//Function for Finding the Way to Exit.
void Find_Way(int i, int j, int row_size, int column_size, char mat[row_size][column_size])
{
    //Entrance
    mat[i][j] = 'x';

    if(i==0){
        i++;
        mat[i][j]='x';
    }
    else if(i==row_size-1){
        i--;
        mat[i][j]='x';
    }
    else if(j==0){
        j++;
        mat[i][j] = 'x';
    }
    else if(j==column_size-1){
        j--;
        mat[i][j]='x';
    }

    //Loop for Finding Way
    while(j>0 && j<column_size-1 && i>0 && i<row_size-1){
        if(mat[i][j-1]=='x'){ // Face Right
            if(mat[i+1][j]=='.'){ //Move Right
                i++;
                mat[i][j]='x';
            }
            else if(mat[i][j+1]=='.'){ //Move Straight
                j++;
                mat[i][j]='x';
            }
            else if(mat[i-1][j]=='.'){ //Move Left
                i--;
                mat[i][j]='x';
            }
            else{ //Reverse Move
                mat[i][j]='0';
                j--;
            }
        }
        else if(mat[i-1][j]=='x'){ //Face Down
            if(mat[i][j-1]=='.'){
                j--;
                mat[i][j]='x';
            }
            else if(mat[i+1][j]=='.'){
                i++;
                mat[i][j]='x';
            }
            else if(mat[i][j+1]=='.'){
                j++;
                mat[i][j]='x';
            }
            else{
                mat[i][j]='0';
                i--;
            }
        }
        else if(mat[i+1][j]=='x'){  //Face UP

            if(mat[i][j+1]=='.'){
                j++;
                mat[i][j]='x';
            }
            else if(mat[i-1][j]=='.'){
                i--;
                mat[i][j]='x';
            }
            else if(mat[i][j-1]=='.'){
                j--;
                mat[i][j]='x';
            }
            else{
                mat[i][j]='0';
                i++;
            }
        }
        else{     //Face Left
            if(mat[i-1][j]=='.'){
                i--;
                mat[i][j]='x';
            }
            else if(mat[i][j-1]=='.'){
                j--;
                mat[i][j]='x';
            }
            else if(mat[i+1][j]=='.'){
                i++;
                mat[i][j]='x';
            }
            else{
                mat[i][j]='0';
                j++;
            }
        }
    }

}

int main()
{
    //Creating Main File of Project
    FILE *maze_file;
    int n, m, is ,js , option;

    //Choosing Between Default and Random Options
    printf("Choose:\n1)Default Maze.\n2)Random Handmade Generated Maze.\n");
    scanf("%d",&option);

    //Default Option
    if(option==1) {
        //Opening Default File az Main File of the Project
        maze_file = fopen("default_maze.txt","r");

        //Default Dimensions
        n=12;
        m=12;

        //Default Start Point
        is=2;
        js=0;
    }

    //Random Option
    else if(option==2){

        printf("OK, let's Make it :)\n");

        //Creating Random Maze File
        FILE *rand_maze;
        rand_maze=fopen("rand_maze.txt","w");

        //Get Dimensions from User
        printf("Enter Dimensions(row x column):\n");
        scanf("%d %d", &n, &m);

        //Error Control
        if(n<=2 || m<=2){
            printf("Error: Invalid Dimension!(At least 3x3) ");
            return 0;
        }

        //Get Entrance Coordinates from User
        printf("Enter Entrance Coordinates (row,column): \n");
        scanf("%d %d", &is, &js);

        //Error Control
        if((is+js <= 0) || (is+js >= n+m-2) || (is==n-1 && js==0) || (is==0 && js==m-1)){
            printf("Error: Invalid Entrance(Corners)! \n");
            return 0;
        }
        if(is!=0 && is != n-1 && js!=0 && js!=m-1){
            printf("Error: Invalid Entrance(Middle)! \n");
            return 0;
        }

        //Creating Matrix for Random Maze
        char rand_mat[n][m];
        Random_Maze_Generator(is,js,n,m,rand_mat,rand_maze);

        //Opening Random File as Main file of the Project
        maze_file = fopen("rand_maze.txt","r");
        fclose(rand_maze);
    }

    //Error Control
    else{
        printf("Error: Wrong Input! \n");
        return 0;
    }


    //Creating Matrix and Copy the Main File to it.
    char M[n][m];
    rewind(maze_file);
    File_to_Matrix(maze_file,n,m,M);
    fclose(maze_file);

    // Finding way to Exit.
    Find_Way(is, js, n, m, M);

    // Create File for GUI.
    FILE *GUI;
    GUI = fopen("GUI.txt","w");
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            fprintf(GUI,"%c",M[i][j]);
        }
        fprintf(GUI,"\n");
    }
    fclose(GUI);

    //Preparing for print result(change 0 to x).
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
            if (M[x][y] == '0') M[x][y] = 'x';
        }
    }

    //Print Result.
    printf("The Result Maze is : \n");
    for(int x=0;x<n;x++) {
        for (int y = 0; y < m; y++) {
            printf("%c  ", M[x][y]);
        }
        printf("\n");
    }
    return 0;
}