// Containers in stl c++


void explainPair(){
  pair<int, int> p = {1,3};
  cout << p.first << " " << p.second; // output: 1 3

  pair <<int, pair<int, int>> p = {1, {2, 3}};
  cout << p.first << " " << p.second.second << p.second.first; // output: 1 32

  pair<int, int> arr[] = { {1, 2}, {3, 4}, {4, 5}}
  cout << arr[1].second; //output: 4
}


void explainVector(){
  // vector has a dynamic size, while array has a fixed size
  vector<int> v;

  v.push_back(1); // v = {1}
  v.emplace_back(2); // v = {1,2}


  vector<int> v(5, 100); // v = {100, 100, 100, 100, 100};

  vector<pair<int, int>> vec;

  vec.push_back({1, 2}); // vec = { {1, 2} }
  vec.emplace_back({3, 4}); // vec = { {1, 2}, {3, 4}}

  vector<int> v(5); // -> this will create a vector of size 5

  vector<int> v1(5, 20);
  vector<int> v2(v1); // -> this copy all the elements to v2 from v1

  // Iterators

  vector<int> v{1, 2, 3, 4};
  vector<int>::iterator it = v.begin(); // -> the begin method points to the first address of the first element in the vector
  it++;
  cout << *(it) << " "; // output: 2

  it = it + 2;
  cout << *(it) << " "; // output: 4

  vector<int>::iterator it = v.end();
  vector<int>::iterator it = v.rbegin();
  vector<int>::iterator it = v.rend();

  cout << v[0] << " " << v.at(0); // output: 1
  cout << v.back() << " "; // output: 4

  // how to loop through a vector - 2 ways
  // auto - automatically assigns a data type to the variable based on the data
  
  for(vector<int>::iterator it = v.begin(); it != v.end(); it++){
      cout << *(it);
  }
  
  for(auto it = v.begin(); it != v.end(); it++{
      cout << *(it);
  }
  // for each loop
  for(auto it: v){
      cout << it << " ";
  }


  // Deleting
  //{10, 20, 30, 40}
  v.erase(v.begin() + 1); -> {20, 30,40}

  // {10, 20, 30, 40, 50}
  v.erase(v.begin() + 2, v.begin() + 4); // {10, 20, 50}


  // Insert Function
  vector<int> v(2, 100); //{100, 100}
  v.insert(v.begin(), 300); // {300, 100, 100}
  v.insert(v.begin() + 1, 2, 10); // {300, 10, 10, 100, 100}

  vector<int> copy(2, 50);
  v.insert(v.begin(), copy.begin(). copy.end()); // {50, 50, 300, 10, 10, 100, 100}

  // {10, 10}
  cout << v.size(); // 2
  
  // {10, 20}
  v.pop_back(); // {10}
  
  
  






  
  
  
  
}

