操作步骤：  
1）打开case.xls文件，填写url，是否运行，请求类型，headers，以及后面的测试依赖用例相关信息和预期结果；  
2）打开cookies.json，写入相应的信息；  
3）打开data.json，写入相应的信息；  
4）执行main.py；  
5) 屏幕上会让输入一些必要的信息，带*部分，必须要用户手动输入参数。其他参数，可以按回车键，选择默认参数。

Operation steps:
1) Open case.xls file, write some informations like url, run or not, method, headers, associate case and expect result and so on;
2) Open cookies.json file, input cookies information;
3) Open data.json file, input data information;
4) Excute python main.py；
5）About the questions shown on the screen, the * questions are needed，otherwise，you can press enter and the deault value will be selected.


说明：  
case.xls的case用例，前三个是我用fiddler模拟出来，并不是真实存在的；  
后面的case用例，是我在测试项目中，选出来的几个。你并不可以拿来直接运行。

Explain:
The cases shown on case.xls are not going to work directly from your side.


遗留的问题：  
1.当存在数据依赖的时候，暂时只支持只存在一个数据依赖的情况。    
2.目前只在get和post请求方法上验证通过，put，delete，head，options，trace，connect，目前没有适合的接口验证。  


Issues:
1. Until now, only one dependent parameter is supported.
2. By far, the get and post method can be run successfully. about others, i did not verify.













# Test
