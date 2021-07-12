#include<bits/stdc++.h>
using namespace std;

vector< vector<int> > X,Y,T;
int input = 3,output = 2;
vector<int> truthTest;
int confutionMatrix[1000][1000];

ifstream fi("training.INP");
ifstream fii("testing.INP");

map< string, int > toIntFeature[100];
map<int, string> toStringFeature[100];

void GetTraining(){
	string x;
	map<string, int> exists;
	exists.clear();
	int k = 1;
	int kk[100];
	for(int i = 0;i <= input;i++)kk[i] = 1;
	while(fi>>x){
            vector < int > v,vv;
            if(!toIntFeature[0][x])toIntFeature[0][x] = kk[0]++;
            v.push_back(toIntFeature[0][x]);
            toStringFeature[0][toIntFeature[0][x]] = x;
            for(int i = 1;i < input;i++)
            {
                fi>>x;
                if(!toIntFeature[i][x])toIntFeature[i][x] = kk[i]++;
                v.push_back(toIntFeature[i][x]);
                toStringFeature[i][toIntFeature[i][x]] = x;
            }
            //for(int i = 0;i < output;i++)fi>>x,vv.push_back(x);
            fi>>x;
            if(!exists[x]) exists[x] = k++;
            vv.push_back(exists[x]);
            toStringFeature[input+1][exists[x]] = x;
            X.push_back(v);
            Y.push_back(vv);
	}
}

void GetTesting(){
	string x;
	while(fii>>x){
        vector < int > v;
        v.push_back(toIntFeature[0][x]);
        for(int i = 1;i < input;i++)
            fii>>x,v.push_back(toIntFeature[i][x]);
		T.push_back(v);
	}
}


// traing 80%, testing 20%
map<int,bool> isTest;

void GetTestingFromTraining()
{
    int test = 0.2*X.size();
    while(test--)
    {
        int t = rand()%X.size();
        while(1)
        {
            if(!isTest[t])
            {
                isTest[t] = true;
                T.push_back(X[t]);
                truthTest.push_back(Y[t][0]);
                break;
            }
            t = rand()%X.size();
        }
    }
}

struct F
{
    double val[100][100];
};

vector< F > pA;
double pS[100];

void NaiveBayes()
{
    int numFeature = X[0].size();
    for(int i = 0;i < numFeature;i++)
    {
        F f;
        for(int i = 0;i <= output;i++)pS[i] = 0;
        for(int i = 0;i < Y.size();i++)
            pS[Y[i][0]]++;

        for(int j = 1;j <= X.size();j++)
            for(int k = 1;k <= output;k++)
                f.val[j][k] = 0;

        for(int j = 0;j < X.size();j++)
        {
            f.val[X[j][i]][Y[j][0]]++;
        }
        for(int j = 1;j <= X.size();j++)
            for(int k = 1;k <= output;k++)
                f.val[j][k] /= pS[k];

        for(int i = 1;i <= output;i++)pS[i] /= Y.size();

        pA.push_back(f);
    }
}

void Test()
{
    for(int i = 0;i < T.size();i++)
    {
        double ma = -1;
        int layout = -1;
        for(int j = 1; j <= output;j++)
        {
            double bayes = 1;
            for(int k = 0;k < T[i].size();k++)
            {
                bayes *= pA[k].val[T[i][k]][j];
               // cout<<pA[k].val[T[i][k]][j]<<endl;
            }
            if(ma < bayes/pS[j]) ma = bayes*pS[j], layout = j;
        }
        for(int j = 0;j < T[i].size();j++)cout<<toStringFeature[j][T[i][j]]<<" ";
        cout<<"-> "<<toStringFeature[input+1][layout]<<endl;

       // confutionMatrix[truthTest[i]][layout]++;
    }
}

void ShowConfusionMatrix()
{
    int corectLabel = 0;
    cout<<endl<<"Confusion Matrix:"<<endl;
    cout<<"        Prediction"<<endl;
    cout<<"      ___";
    for(int i = 1;i <= output-1;i++)
        cout<<i<<"___";
        cout<<output<<"__";
    cout<<endl<<"Truth ";
    for(int i = 1;i <= output;i++)
    {
        cout<<i<<char(179)<<" ";
        for(int j = 1;j <= output;j++)
        {
            cout<<confutionMatrix[i][j]<<"   ";
            if(i == j)corectLabel+= confutionMatrix[i][j];
        }
        cout<<endl<<"      ";
    }

    cout<<endl<<"Accuracy: "<< corectLabel*100/T.size()<<"%"<<endl;

}


main()
{

    srand(time(NULL));
    GetTraining();
    GetTesting();
    //GetTestingFromTraining();
    NaiveBayes();
    Test();
   // ShowConfusionMatrix();
    fi.close();
    fii.close();

}

