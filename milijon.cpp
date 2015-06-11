#include <vector>
#include <ctime>
#include <random>
#include <iostream>
#include <cmath>
using namespace std;

#define PI 3.14159

class zvezda{
public:
	float m;//masa
	float x,y,z;//pozicija
	float vx,vy,vz;//hitrost
	zvezda() :x(0), y(0),z(0),vx(0),vy(0),vz(0), m(1){}
};

mt19937_64 generator;
uniform_real_distribution<float> mass(0.1, 1.0);
uniform_real_distribution<float> rad(0.00001, 50.0);
uniform_real_distribution<float> angle(0.0, 2 * PI);
uniform_real_distribution<float> z(-0.7, 0.7);
vector<zvezda> gen(int n){
	vector<zvezda> data(n);
	float sumx = 0, sumy = 0, sumz = 0;
	for (int i = 0; i < n; i++){
		data[i].m = 1;// mass(generator);
		float r = rad(generator);
		float a = angle(generator);
		a += sin(10 * PI*a);
		data[i].x = r*cos(a);
		data[i].y = r*sin(a);
		data[i].z = 0;// z(generator);
		sumx += data[i].x*data[i].m;
		sumy += data[i].y*data[i].m;
		sumz += data[i].z*data[i].m;
		data[i].vx = data[i].y/r *1.2;
		data[i].vy = -data[i].x/r *1.2;
		data[i].vz = 0;
		/*for (int j = 0; j < i; j++){
			if (abs(data[j].x - data[i].x)<0.001 &&
				abs(data[j].y - data[i].y)<0.001){
				cout << i << " " << j << "\n";
			}
		}*/
	}
	sumx /= n;
	sumy /= n;
	sumz /= n;
	for (int i = 0; i < n; i++){//skupno tezisce je pri miru
		data[i].x -= sumx/data[i].m;
		data[i].y -= sumy / data[i].m;
		data[i].z -= sumz / data[i].m;
	}
	return data;
}

float G=1;//"gravitacijska konstanta"

void update(vector<zvezda> &data, float step = 0.1){
	for (int i = 0; i<data.size(); i++){
		for (int j = 0; j<data.size(); j++){
			if (i != j){
				float dx = data[j].x - data[i].x;
				float dy = data[j].y - data[i].y;
				float dz = data[j].z - data[i].z;
				float temp = G*step*data[i].m*pow(dx*dx + dy*dy + dz*dz, -1.5f);// **0.5 **3 **-1
				temp = temp < 0.05*step ? temp : 0.05*step;
				data[i].vx += temp*dx;
				data[i].vy += temp*dy;
				data[i].vz += temp*dz;
			}
		}
	}
	for (int i = 0; i < data.size(); i++){
		data[i].x += step*data[i].vx;
		data[i].y += step*data[i].vy;
		data[i].z += step*data[i].vz;
	}
}


void test(){
	vector<zvezda> data = gen(2000);
	for (int i = 0; i < 10; i++){
		clock_t t = clock();
		update(data);
		cout << (double)(clock() - t) / CLOCKS_PER_SEC << "\n";
	}
}

int main(){
	test();
	int i;
	cin >> i;
	return 0;
}