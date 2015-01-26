centroids = dlmread('Centroid_File',',');

dirData2 = dir('dataset/feats/test'); 
dirIndex2 = [dirData2.isdir];
subDirs2 = {dirData2(dirIndex2).name};

index2 = subDirs2(3:end);

vector1 = [];
vector2 = [];
    
test = 50;

     
    a = index2(test);
    
    a = a{:};
     b = strcat('dataset/feats/test/',a);
     fileList = getAllFiles(b);

   
    a = fileList(1);
    a = a{:};
    A = dlmread(a,' ');
    vector1 = [ vector1; A ];
    
    a = fileList(2);
    a = a{:};
    A = dlmread(a,' ');
    vector1 = [ vector1; A ];
    

    


p = [];
min_in1 = -1;
min1 = 10^10;
array= zeros(1,630);

for j=1:length(vector1)
    for i=1:length(centroids)
         dist = norm(centroids(i,:)-vector1(j,:));
        if dist < min1;
            min1 = dist;
            min_in1 = i;
        end
    end
    min_in1;
    new_index = ((32 - mod(min_in1,32)) + min_in1)/32;
    array(1,new_index) = array(1,new_index) + 1 ;
 end

 [a,ans_in1] = max(array);



test
 ans_in1
display('correct')
disp(index2(test))
display('Ouput')
disp(index2(ans_in1))

