#include <vector>
#include <ctime>
#include <iostream>
using namespace std;


class zvezda{
public:
	float m;//masa
	float x,y,z;//pozicija
	float vx,vy,vz;//hitrost
	zvezda() :x(0), y(0),z(0),vx(0),vy(0),vz(0), m(1){}
};

vector<zvezda> gen(int n = 100){
	return vector<zvezda>(n);
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
	clock_t t = clock();
	update(data);
	cout << data.size() << "\n";
	cout << (double)(clock() - t) / CLOCKS_PER_SEC << "\n";
}

int main(){
	test();
	int i;
	cin >> i;
	return 0;
}