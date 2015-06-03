#include<stdlib.h>
#include<string.h>
#include <iostream>
#include <cmath>
#include <GL/glut.h>
using namespace std;

#define PI 3.141592653589
#define DEG2RAD(deg) (deg * PI / 180)

//spider defination
typedef struct spider
{
    float x;
    float y;
    float vel;
    int h;
    int rest;
}spider;

spider spi[100];
// Function Declarations
void drawScene();
void update(int value);
void drawWorld(float wid,float ht);
void drawRect(float wid,float ht);
void drawBox(float len);
void drawLine();
void drawSpider();
void handleKeypress1(unsigned char key, int x, int y);
void processSpecKeys(int key, int x, int y);
void drawTriangle();
void initRendering();
void handleResize(int w, int h);
void handleMouseclick(int button, int state, int x, int y);
void motion(int x, int y);
void motionPassive(int x, int y);
void entry(int state);
void scoredisplay (float posx, float posy, float posz, float space_char, int scorevar);
void displayletters (float posx, float posy, float posz, float space_char, char *s);
void drawBall(float rad);
void drawRedBasket(float rad);
void drawGreenBasket(float rad);


// Global Variables
int keys[256] = {0};

float windowWidth = 0.0f;
float windowHeight = 0.0f;
float world_len = 0.0f;
float world_ht = 0.0f;
float base_len = 0.0f;
float base_ht = 0.0f;
float bas_len = 0.0f;		//basket
float green_x = 0.0f ;
float green_y = 0.0f;
float red_x = 0.0f;
float red_y = 0.0f;
float canon_x = 0.0f;
float canon_y = 0.0f ;
float theta = 0.0f;
float canon_len = 0.0f;
float canon_ht = 0.0f ;
float gun_len = 0.0f;
float gun_ht = 0.0f;

int laser_time = 0;
float laser_len = 0.0f;
float laser_base_x = 0.0f;
float laser_base_y = 0.0f;
float laser_theta = 0.0f;
float laser_x1 = 0.0f;
float laser_y1 = 0.0f;
float laser_x2 = 0.0f;
float laser_y2 = 0.0f;
float laser_vel = 0.0f;
float laser_vel_x = 0.0f;
float laser_vel_y = 0.0f;


float spi_len = 0.0f;
int score = 0;
int spi_rest =0;
int spi_count = 0;
float spi_min_vel = 0.0f;
float spi_max_vel = 0.0f;

bool flag = 0;	//intializations
int game = 1;	//0 --> over; 1 --> play; 2-->paused;
int game_time =0;

float green_limit_1 = 0.0f;
float green_limit_2 = 0.0f;
float red_limit_1 =  0.0f;
float red_limit_2 =  0.0f;
float canon_limit_1 = 0.0f;
float canon_limit_2 =  0.0f;

float mouse_x = 0.0f;
float mouse_y = 0.0f;
bool mleft = 0;
bool mright = 0;
//main function
int main(int argc, char **argv) {

    // Initialize GLUT
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);


    float w = glutGet(GLUT_SCREEN_WIDTH);
    float h = glutGet(GLUT_SCREEN_HEIGHT);
    windowWidth = w * 2 / 3;
    windowHeight = h * 2 / 3;

    cin >> world_len >> world_ht >> bas_len >> canon_len >> canon_ht >> gun_len >> gun_ht >> laser_vel >> spi_len >> spi_count>> spi_min_vel >> spi_max_vel;
    base_len = world_len;
    base_ht = world_ht / 10;
    green_x = -world_len/2 + 0.1f + bas_len ;
    green_y = base_ht + bas_len;
    red_x = world_len/2 - 0.1f - bas_len ;
    red_y = base_ht + bas_len;
    canon_x = 0.0f;
    canon_y = base_ht ;
    gun_ht += canon_ht;
    laser_len = 0.1*world_ht;
    green_limit_1 = -world_len/2 + 0.1f;
    green_limit_2 = world_len/2 - 0.1f;
    red_limit_1 = -world_len/2 + 0.1f;
    red_limit_2 = world_len/2 - 0.1f;
    canon_limit_1 = -world_len/2 + 0.1f;
    canon_limit_2 = world_len/2 - 0.1f;


    glutInitWindowSize(windowWidth, windowHeight);
    glutInitWindowPosition((w - windowWidth) / 2, (h - windowHeight) / 2);

    glutCreateWindow("Assignment 1");  // Setup the window
    initRendering();

    // Register callbacks
    glutDisplayFunc(drawScene);
    glutIdleFunc(drawScene);
    
    glutKeyboardFunc(handleKeypress1);
	glutSpecialFunc(processSpecKeys);
    glutMouseFunc(handleMouseclick);
    glutMotionFunc(motion);
    glutPassiveMotionFunc(motionPassive);
    //    glutEntryFunc(entry);
    glutReshapeFunc(handleResize);
    if(game==1)
    {
	glutTimerFunc(10, update, 0);
      //  system("aplay background.wav &");
    }
//	PlaySound(TEXT("keyboard.wav"), NULL, SND_FILENAME | SND_ASYNC);
//	PlaySound(TEXT("MyAppSound"), NULL, SND_APPLICATION);

    if(flag == 0)
    {
	int i=0;
	for(i=0;i<spi_count;i++)
	{

	    float a = world_len/2 - 0.2f;
	    float x1 = (float)rand()/(float)(RAND_MAX/a);
	    int b = rand() % 100;
	    int d = 1;
	    if(b%2==0)
		d = -1;

	    spi[i].x = x1*d;
	    spi[i].y = world_ht;
	    spi[i].h = rand()%3+1;
	    spi[i].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
	    if(spi[i].vel==0)
		spi[i].vel = 0.18f;
	    spi[i].rest = 1;
	}

	flag = 1;
    }
    //runs every 10 milli sec
    glutMainLoop();
    return 0;
}

// Function to draw objects on the screen
void drawScene() {

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW); //positions and drawings
    glLoadIdentity(); //loads identity matrix into the stack
    glPushMatrix();

    // Draw world
    glTranslatef(0.0f, -world_ht/2, -5.0f);
    glColor3f(0.8f, 1.0f, 0.8f);
    drawWorld(world_len,world_ht);

    //draw base

    glColor3f(0.9f, 0.7f, 0.2f);
    drawRect(base_len,base_ht);


    //draw green basket
    glPushMatrix();
    glTranslatef( green_x, green_y, 0.0f);
    if(keys['g']==0)
	glColor3f(0.4f, 1.0f, 0.4f);
    else
	glColor3f(0.0f,1.0f,0.0f);
    drawGreenBasket(bas_len);
    glPopMatrix();

    //draw red basket
    glPushMatrix();
    if(keys['r']==0) 
	glColor3f( 1.0f,  0.4f, 0.4f);
    else
	glColor3f(1.0f,0.0f,0.0f);
    glTranslatef( red_x,red_y, 0.0f);
    drawRedBasket(bas_len);
    glPopMatrix();


    //draw canon
    glPushMatrix();
    if(keys['b']==1)
	glColor3f(0.0f,0.0f,1.0f);
    else
	glColor3f(0.2f,0.4f,0.6f);
    glTranslatef(canon_x,canon_y, 0.0f);
    //    drawTriangle();
    drawRect(canon_len,canon_ht);
    glPushMatrix();
    glTranslatef(0.0f,0.05f, 0.0f);
    glRotatef(theta, 0.0f, 0.0f, 1.0f);
    drawRect(gun_len,gun_ht);
    glPopMatrix();
    glPopMatrix();

   /* glPushMatrix();
    glTranslatef(-canon_len/2,0.0f, 0.0f);
    drawRect(0.1f,gun_ht/2);
    glPopMatrix();
*/
    //draw laser
    if(keys[' ']==1)
	drawLine();

    // draw spider
    if(game!=0)
	drawSpider();    

    //display score
//    if(game!=1)
  //  {
	glPushMatrix();
	glTranslatef(5.0f,5.0f,-5.0f);
	scoredisplay(0.0f,0.0f,0.0f,0.2f,score);
	glPopMatrix();
   // }
    if(game==0)
    {
	displayletters(-1.0f,world_ht/2,-5.0f,2.0f,"GAME OVER");
	scoredisplay(0.0f,world_ht/2 - 0.5f,-5.0f,0.2f,score);
    }




    glPopMatrix();
    glutSwapBuffers();
}

// Function to handle all calculations in the scene
// updated evry 10 milliseconds
void update(int value) {
    if(game==1)
    {
	int i=0;
	//counting gaame time
	game_time ++;

	if(game_time >= 500)
	{
	    spi_max_vel += 0.001f;
	    spi_min_vel += 0.002f;
	    laser_vel += 0.002f;
	    game_time = 0;
	    int k;
	    for(k=spi_count;k<spi_count+1;k++)
	    {
	    float a = world_len/2 - 0.2f;
	    float x1 = (float)rand()/(float)(RAND_MAX/a);
	    int b = rand() % 100;
	    int d = 1;
	    if(b%2==0)
		d = -1;

	    spi[k].x = x1*d;
	    spi[k].y = world_ht;
	    spi[k].h = rand()%3+1;
	    spi[k].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
	    if(spi[k].vel==0)
		spi[k].vel = 0.18f;
	    spi[k].rest = 1;

	    }
	    spi_count += 1;
	}
	//counting upto one second
	if(keys[' ']==1)
	    laser_time++;

	//laser wall collision    


	if(keys[' ']==1 &&  laser_y2 >= world_ht - base_ht)
	{
	    laser_x1 = 0.0f;
	    laser_y1 = 0.0f;
	    laser_x2 = 0.0f;
	    laser_y2 = 0.0f;
	    laser_base_x = canon_x;
	    laser_base_y = canon_y;
	}
	else if(laser_x2>=world_len/2 ) 
	{
	    cout<< " wall"<<endl;
	    laser_theta =  -1 * laser_theta;
	    laser_x1 = laser_x2;
	    laser_y1 = laser_y2;
	    laser_x2 = -1*laser_len*sin(DEG2RAD(laser_theta)) + laser_x1; 
	    laser_y2 = laser_len*cos(DEG2RAD(laser_theta)) + laser_y1;
	    laser_vel_x = -1*laser_vel*sin(DEG2RAD(laser_theta));
	    laser_vel_y = laser_vel*cos(DEG2RAD(laser_theta));
	}
	else if(laser_x2 <= -world_len/2 )
	{
	    cout<< " wall"<<endl;
	    laser_theta =  -1 * laser_theta;
	    laser_x1 = laser_x2;
	    laser_y1 = laser_y2;
	    laser_x2 = -1*laser_len*sin(DEG2RAD(laser_theta)) + laser_x1; 
	    laser_y2 = laser_len*cos(DEG2RAD(laser_theta)) + laser_y1;
	    laser_vel_x = -1*laser_vel*sin(DEG2RAD(laser_theta));
	    laser_vel_y = laser_vel*cos(DEG2RAD(laser_theta));
	}
	//laser vanishing 
	if(laser_time>=100)
	{

	    keys[' '] = 0;
	    laser_time=0;
	    laser_x1 = 0.0f;
	    laser_y1 = 0.0f;
	    laser_x2 = 0.0f;
	    laser_y2 = 0.0f;
	    laser_theta = theta;
	    laser_base_x = canon_x;
	    laser_base_y = canon_y;
	}
	//laser translation
	if(keys[' ']==1)
	{
	    laser_x1 += laser_vel_x;
	    laser_y1 += laser_vel_y;
	    laser_x2 += laser_vel_x;
	    laser_y2 += laser_vel_y;
	}

	//spider translation
	for(i=0;i<spi_count;i++)
	{
	    // red color spider is caught by red basket
	    if(spi[i].rest==1 && spi[i].x - spi_len > red_x-bas_len && spi[i].x + spi_len < red_x + bas_len && spi[i].y - spi_len <= (base_ht+bas_len) )
	    {
		if(spi[i].h==1)
		{
		    score++;
		    system("aplay spider_collect.wav &");
		}
		else if(spi[i].h==2 || spi[i].h==3)
		    score--;
		spi[i].h = rand() % 3 +1;
		float a = world_len/2 - 0.2f;
		float x1 = (float)rand()/(float)(RAND_MAX/a);
		int b = rand() % 100;
		int d = 1;
		if(b%2==0)
		    d = -1;

		spi[i].x = x1*d;
		spi[i].y =world_ht;
		spi[i].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
		//// cout<<"score"<<endl;
	    }

	    //green spider is caught by green spider
	    else if(spi[i].rest==1 && spi[i].x - spi_len > green_x-bas_len && spi[i].x + spi_len < green_x + bas_len && spi[i].y - spi_len <=(base_ht+bas_len))
	    {
		if(spi[i].h==2)
		{
		    score++;
		    system("aplay spider_collect.wav &");
		}
		else if(spi[i].h==1 ||spi[i].h==3)
		    score--;
		spi[i].h = rand() % 3 +1;
		float a = world_len/2 - 0.2f;
		float x1 = (float)rand()/(float)(RAND_MAX/a);
		int b = rand() % 100;
		int d = 1;
		if(b%2==0)
		    d = -1;

		spi[i].x = x1*d;
		spi[i].y =world_ht;
		spi[i].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
		//cout<<"score";
	    }
	    //spider hit by laser
	    if(spi[i].rest==1 && laser_x2 > spi[i].x - 0.09f && laser_x2 < spi[i].x + 0.09f && laser_y2 <= spi[i].y + 0.3f && laser_y2 > spi[i].y - 0.3f)
	    {
		    system("aplay spider_killed.wav &");
		if(spi[i].h==2)
		{
		    score++;
		}
		laser_x1 = 0.0f;
		laser_x2 = 0.0f;
		laser_y1 = 0.0f;
		laser_y2 = 0.0f;

		spi[i].h = rand() % 3 +1;
		float a = world_len/2 - 0.2f;
		float x1 = (float)rand()/(float)(RAND_MAX/a);
		int b = rand() % 100;
		int d = 1;
		if(b%2==0)
		    d = -1;

		spi[i].x = x1*d;
		spi[i].y =world_ht;
		spi[i].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
	    }
	    //translation
	    if(spi[i].rest==1 && spi[i].y > base_ht + spi_len)
	    {
		spi[i].y -= spi[i].vel;
	    }
	    //lands on canon
	    if(spi[i].rest== 1 && canon_x - gun_len/2 - 0.2f < spi[i].x  && canon_x + gun_len/2 + 0.2f > spi[i].x && spi[i].y <= canon_y + canon_ht+ gun_ht/2)
	    {
		    system("aplay game_over.wav &");
		game = 0;
		system("pause");
	    }
	    //rest on base
	    if(spi[i].rest==1 && spi[i].y - 0.15f <= base_ht)
	    {
		score--;
		spi[i].rest =0;
		spi_count += 1;
		spi_rest++;
		spi[spi_count-1].h = rand() % 3 +1;
		float a = world_len/2 - 0.2f;
		float x1 = (float)rand()/(float)(RAND_MAX/a);
		int b = rand() % 100;
		int d = 1;
		if(b%2==0)
		    d = -1;

		spi[spi_count-1].rest = 1;
		spi[spi_count-1].x = x1*d;
		spi[spi_count-1].y =world_ht;
		spi[spi_count-1].vel = (float)rand()/(float)(RAND_MAX/spi_max_vel-spi_min_vel) + spi_min_vel;
	    }
	    //changing movement constraints of red,green baskets and canon

	    if(spi[i].rest==0)
	    {
		//spider --> basket 
		if(spi[i].x - spi_len <= green_x - bas_len && (spi[i].x + spi_len <= green_x - bas_len || spi[i].x + spi_len >= green_x  - bas_len ))
		{	if(spi[i].x + spi_len > green_limit_1)
		    green_limit_1 = spi[i].x + spi_len;
		}
		//   if(spi[i].x - spi_len <= red_x - bas_len  && spi[i].x + spi_len <= red_x - bas_len)
		if(spi[i].x - spi_len <= red_x - bas_len && (spi[i].x + spi_len <= red_x - bas_len || spi[i].x + spi_len >= red_x  - bas_len ))
		{
		    if(spi[i].x + spi_len > red_limit_1)
			red_limit_1 = spi[i].x + spi_len;
		}
		if(spi[i].x - spi_len <= canon_x - canon_len/2  && (spi[i].x + spi_len <= canon_x - canon_len/2 || spi[i].x + spi_len > canon_x - canon_len/2	))
		{
		    if(spi[i].x + spi_len > canon_limit_1)
			canon_limit_1 = spi[i].x + spi_len;
		}
		//basket --> spider
		if((spi[i].x - spi_len >= red_x + bas_len || spi[i].x - spi_len < red_x + bas_len)  && spi[i].x + spi_len >= red_x + bas_len )
		{
		    if(spi[i].x - spi_len < red_limit_2)
			red_limit_2 = spi[i].x - spi_len;
		}
		//if(spi[i].x - spi_len >= green_x + bas_len  && spi[i].x + spi_len >= green_x + bas_len)
		if((spi[i].x - spi_len >= green_x + bas_len || spi[i].x - spi_len < green_x + bas_len)  && spi[i].x + spi_len >= green_x + bas_len )
		{	if(spi[i].x - spi_len < green_limit_2)
		    green_limit_2 = spi[i].x - spi_len;
		}
		if((spi[i].x - spi_len >= canon_x + canon_len/2 || spi[i].x - spi_len < canon_x + canon_len/2)  && spi[i].x + spi_len >= canon_x + canon_len/2)
		{	if(spi[i].x - spi_len < canon_limit_2)
		    canon_limit_2 = spi[i].x - spi_len;
		}

	    }
	}

	    if(spi_rest == 95)
	    {
		game =0;
		spi[99].x = canon_x;
		spi[99].y = world_ht;
		spi[99].h = 1;
		spi[99].vel = 0.04f;
		spi[99].rest = 1;
	    }
	
    }
    glutTimerFunc(10, update, 0);

}
//drawing functions
void drawWorld(float len,float ht) {

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    // glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glBegin(GL_QUADS);
    glVertex2f( -len/2, 0);
    glVertex2f( -len/2, ht);
    glVertex2f( len/2,  ht);
    glVertex2f( len/2, 0);
    glEnd();
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
}

void drawRect(float wid,float ht)
{
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    glBegin(GL_QUADS);
    glVertex2f(-wid / 2, 0);
    glVertex2f(wid / 2, 0);
    glVertex2f(wid / 2, ht );
    glVertex2f(-wid / 2, ht);
    glEnd();
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

}


void drawTriangle() {

    //if(keys['b']==0)
    //	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glBegin(GL_TRIANGLES);
    glVertex3f(0.0f, 0.1f, 0.0f);
    glVertex3f(0.07f, 0.0f, 0.0f);
    glVertex3f(-0.07f, 0.0f, 0.0f);
    glEnd();
}

void drawBall(float rad) {

    glBegin(GL_TRIANGLE_FAN);	//circle is divided into triangles
    for(int i=0 ; i<360 ; i++) {
	glVertex2f(rad * cos(DEG2RAD(i)), rad * sin(DEG2RAD(i)));
    }
    glEnd();
}

void drawRedBasket(float rad) {

    //if(keys['r']==0)
    //	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glBegin(GL_TRIANGLE_FAN);	//circle is divided into triangles
    for(int i=180 ; i<360 ; i++) {
	glVertex2f(rad * cos(DEG2RAD(i)), rad * sin(DEG2RAD(i)));
    }
    glEnd();
}
void drawGreenBasket(float rad) {

    glBegin(GL_TRIANGLE_FAN);	//circle is divided into triangles
    for(int i=180 ; i<360 ; i++) {
	glVertex2f(rad * cos(DEG2RAD(i)), rad * sin(DEG2RAD(i)));
    }
    glEnd();
}
void drawLine()
{
    glColor3f(0.0f,0.0f,1.0f);
    glPushMatrix();
    glTranslatef(0.0f,canon_ht,0.0f);
    glBegin(GL_LINES);
    glVertex3f(laser_x1,laser_y1,0.0f);
    glVertex3f(laser_x2,laser_y2,0.0f);
    glEnd();
    glPopMatrix();
}
void drawSpider()
{

    int i=0;
    for(i=0;i<spi_count;i++)
    {
	if(spi[i].h==1)
	    glColor3f(1.0, 0.0, 0.0);
	else if(spi[i].h==2)
	    glColor3f(0.0, 1.0, 0.0);
	else 
	    glColor3f(0.0, 0.0, 0.0);

	glPushMatrix();
	glTranslatef(spi[i].x,spi[i].y,0.0f);
	drawBall(0.1f);

	glPushMatrix();
	glTranslatef(0.0f,-0.12f,0.0f);
	drawBall(0.07f);

	glPushMatrix();
	glTranslatef(-0.06f,0.03f,0.0f);
	glBegin(GL_LINES);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(-0.1f,0.0f,0.0f);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(-0.1f,-0.1f,0.0f);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(-0.1f,0.1f,0.0f);
	glEnd();
	glPopMatrix();


	glPushMatrix();
	glTranslatef(0.06f,0.03f,0.0f);
	glBegin(GL_LINES);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(0.1f,0.0f,0.0f);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(0.1f,0.1f,0.0f);
	glVertex3f(0.0f,0.0f,0.0f);
	glVertex3f(0.1f,-0.1f,0.0f);
	glEnd();
	glPopMatrix();
	

	glPushMatrix();
	glColor3f(0.9f,1.0f,0.0f);
	glTranslatef(0.03f,-0.001f,0.0f);
	drawBall(0.009f);
	glPopMatrix();
	
	glPushMatrix();
	glColor3f(1.0f,1.0f,1.0f);
	glTranslatef(-0.03f,-0.001f,0.0f);
	drawBall(0.009f);
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();
    }
}

// Initializing some openGL 3D rendering options
void initRendering() {

    glEnable(GL_DEPTH_TEST);        // Enable objects to be drawn ahead/behind one another
    glEnable(GL_COLOR_MATERIAL);    // Enable coloring
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   // Setting a background color
}

// Function called when the window is resized
void handleResize(int w, int h) {

    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, (float)w / (float)h, 0.1f, 200.0f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}
//called when any keyboard key is pressed
void handleKeypress1(unsigned char key, int x, int y) {

    if (key == 27) {
	{
		system("pause");
	    exit(0);     // escape key is pressed
	}
    }
    if(game==1)
    {
    if(key=='r')
    {
	keys['r'] = 1;
	keys['b'] = 0;
	keys['g'] = 0;
    }
    else if(key=='g')
    {
	keys['r'] = 0;
	keys['b'] = 0;
	keys['g'] = 1;
    }
    else if(key=='b')
    {
	keys['b'] = 1;
	keys['g'] = 0;
	keys['r'] = 0;
    }
    else if( laser_time ==0  && key == ' ' && keys[' ']==0)
    {
	laser_x1 = canon_x;
	laser_y1 = canon_y;
	laser_theta = theta;
	laser_base_x = canon_x;
	laser_base_y = canon_y;
	laser_x2 = -1*laser_len*sin(DEG2RAD(laser_theta)) + laser_x1; 
	laser_y2 = laser_len*cos(DEG2RAD(laser_theta)) + laser_y1;
	laser_vel_x = -1*laser_vel*sin(DEG2RAD(laser_theta));
	laser_vel_y = laser_vel*cos(DEG2RAD(laser_theta));
	keys['r'] = 0;
	keys['c'] = 0;
	keys['g'] = 0;
	keys[' '] = 1;
	system("aplay laser.wav &");
    }
    }
    if(key == 'p')
    {
	if(game==2)
	    game = 1;
	else if(game==1)
	    game = 2;
    }

}
//called when any special key(up,down,left,right arrows) is pressed
void processSpecKeys(int key, int x, int y) {

if(game==1)
{
    if (key == GLUT_KEY_LEFT)
    {

	if(keys['r']==1 && (red_x - bas_len) >= red_limit_1)
	    red_x -= 0.1f;

	if(keys['g']==1 && (green_x - bas_len) >= green_limit_1)
	    green_x -= 0.1f;

	if(keys['b']==1 && (canon_x - canon_len/2) >= canon_limit_1)
	    canon_x-=0.1f;
    }
    else if (key == GLUT_KEY_RIGHT)
    {
	if(keys['r']==1 && (red_x + bas_len) <= red_limit_2)
	    red_x += 0.1f;

	if(keys['g']==1  && (green_x + bas_len) <= green_limit_2)
	    green_x += 0.1f;

	if(keys['b']==1  && (canon_x + canon_len/2) <= canon_limit_2)
	    canon_x+=0.1f;
    }
    else if(key == GLUT_KEY_UP)
    {
	if(keys['b']==1)
	    theta -= 15;
    }
    else if(key== GLUT_KEY_DOWN)
    {
	if(keys['b']==1)
	    theta += 15;
    }
}
}

//mouse clicks 
void handleMouseclick(int button, int state, int x, int y) {
if(game==1)
{
    if (button == GLUT_RIGHT_BUTTON)
    {
	if (state == GLUT_DOWN)
	{
	    cout << "Right button pressed"
		<< endl;
	    mright = 1;
	    mleft = 0;
	}
	else
	{
	    cout << "Right button lifted "
		<< "at (" << x << "," << y
		<< ")" << endl;
	    mright = 0;
	}
    }
    else if (button == GLUT_LEFT_BUTTON)
    {
	if (state == GLUT_DOWN)
	{
	    cout << "Left button pressed"
		<< endl;
	    mleft = 1;
	    mright = 0;
	    if(mouse_x >= green_x - bas_len - 0.25f && mouse_x <= green_x + bas_len + 0.25f && mouse_y <= green_y + 0.25f && mouse_y >= green_y - bas_len - 0.25f)
	    {
		keys['g']=1;
		keys['r']=0;
		keys['b']=0;
	    }
	    else if(mouse_x >= red_x - bas_len - 0.25f && mouse_x <= red_x + bas_len + 0.25f && mouse_y <= red_y + 0.25f && mouse_y >= red_y - bas_len - 0.25f)
	    {
		keys['g']=0;
		keys['r']=1;
		keys['b']=0;
	    }
	    else if(mouse_x >= canon_x - canon_len/2  && mouse_x <= canon_x + canon_len/2  && mouse_y <= canon_y + gun_ht  && mouse_y >= canon_y  )
	    {
		keys['g']=0;
		keys['r']=0;
		keys['b']=1;
		cout<<"on blue"<<endl;
	    }
	}
    }

    else
    {
	cout << "Left button lifted "<<endl;
	mleft = 0;
    }
}
}
void motion(int x, int y)
{
    if(game==1)
    {
    mouse_x = x;
    mouse_y=y;
    windowHeight = glutGet(GLUT_WINDOW_HEIGHT);
    windowWidth = glutGet(GLUT_WINDOW_WIDTH);

    mouse_x = mouse_x - (windowWidth/2) ;
    mouse_x = (mouse_x*6.0f) / windowWidth;
    mouse_y = (windowHeight) - mouse_y ;
    mouse_y = (mouse_y*4.0f) / windowHeight;
    if (mleft)
    {	  //  		cout << "Mouse dragged with left button at "


	//	cout<<"left pressed"<<endl; 
	if(keys['g']==1)

	{
	//    cout<<"g"<<endl;
	    if(mouse_x > green_limit_1 && mouse_x < green_limit_2)
	    {
		if(green_x < mouse_x)
		    green_x = mouse_x - bas_len;
		else
		    green_x = mouse_x + bas_len;
	    }
	    else
	    {
		if(green_x < mouse_x)
		    green_x = green_limit_2 - bas_len;
		else
		    green_x = green_limit_1 + bas_len;
	    }


	}
	else if(keys['r']==1)

	{
	    //	    cout<<"r"<<endl;
	    if(mouse_x > red_limit_1 && mouse_x < red_limit_2)
	    {
		if(red_x < mouse_x)
		    red_x = mouse_x - bas_len;
		else
		    red_x = mouse_x + bas_len;
	    }
	    else
	    {
		if(red_x < mouse_x)
		    red_x = red_limit_2 - bas_len;
		else
		    red_x = red_limit_1 + bas_len;
	    }

	}
	else if(keys['b']==1)

	{
	    //	    cout<<"r"<<endl;
	    if(mouse_x  > canon_limit_1 && mouse_x  < canon_limit_2)
	    {
		if(canon_x < mouse_x)
		    canon_x = mouse_x - canon_len/2;
		else
		    canon_x = mouse_x + canon_len/2;
	    }
	    else
	    {
		if(canon_x  < mouse_x)
		    canon_x = canon_limit_2 - canon_len/2;
		else
		    canon_x = canon_limit_1 + canon_len/2;
	    }

	}
    }

    else if(mright==1)
    {
	if(keys['b']==1)
	{
	    if(canon_x < mouse_x && theta > -89)
		theta -= 1;
	    else if( theta < 89)
		theta += 1;
	    cout << theta << endl;

	}
    }
    }
}
void motionPassive(int x, int y)
{
    mouse_x = x;
    mouse_y=y;

    // Scale to window realEstate
    windowHeight = glutGet(GLUT_WINDOW_HEIGHT);
    windowWidth = glutGet(GLUT_WINDOW_WIDTH);

    mouse_x = mouse_x - (windowWidth/2) ;
    mouse_x = (mouse_x*6.0f) / windowWidth;
    mouse_y = (windowHeight) - mouse_y ;
    mouse_y = (mouse_y*4.0f) / windowHeight;

}
//function to display score
void scoredisplay (float posx, float posy, float posz, float space_char, int scorevar)
{
    int j=0,p,o,n;
    GLvoid *font_style1 = GLUT_BITMAP_TIMES_ROMAN_24;

    p = scorevar;
    if(p<0)
    {
	p *= -1;
	if(p<9)
	    n=1;
	else if(p<99) 
	    n= 2;
	else if(p<999) 
	    n=3;
	else n = 5;

	glColor3f(0.0f,0.0f,0.0f);
	glRasterPos3f ((posx-(0.2f*n)-(j*space_char)),posy, posz);   
	glutBitmapCharacter(font_style1,45);
    }
    j = 0;
    o = 0;
    while(p > 9)
    {
	o = p%10;
	glColor3f(0.0f,0.0f,0.0f);
	glRasterPos3f ((posx-(j*space_char)),posy, posz);   
	glutBitmapCharacter(font_style1,48+o);
	j++;
	p=p/10;
    }
	glColor3f(0.0f,0.0f,0.0f);
    glRasterPos3f ((posx-(j*space_char)), posy, posz);   
    glutBitmapCharacter(font_style1,48+p);
}
void displayletters(float posx, float posy, float posz, float space_char, char *s)
{
    GLvoid *font_style1 = GLUT_BITMAP_TIMES_ROMAN_24;
    int i=0,j=0;

	glColor3f(0.0f,0.0f,0.0f);
    glRasterPos3f(posx,posy, posz);   
    for(i=0;i<strlen(s);i++)
    {
	glutBitmapCharacter(font_style1,s[i]);
	j++;
    }

}


/*

   glBegin(GL_POLYGON);
   GLUquadricObj *obj = gluNewQuadric();

   gluCylinder(obj, 1.0, 1, 3, 30, 30);

   glEnd();
   if(mouse_x >= green_x - bas_len - 0.25f && mouse_x <= green_x + bas_len + 0.25f && mouse_y <= green_y + 0.25f && mouse_y >= green_y - bas_len - 0.25f)

   if(mouse_x + spi_len >= green_limit_1 && mouse_x - spi_len <= green_limit_2)
   {
   if(green_x < mouse_x)
   green_x = mouse_x - bas_len;
   else
   green_x = mouse_x + bas_len;
   }
   else
   {
   if(green_x < mouse_x)
   green_x = green_limit_2 - bas_len;
   else
   green_x = green_limit_1 + bas_len;
   }
 */
