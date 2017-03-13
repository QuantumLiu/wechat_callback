# wechat_callback<br />
可移步知乎专栏查看详情https://zhuanlan.zhihu.com/p/25670072
## Requirement
  itchat<br />
  keras<br />
  numpy<br />
  scipy<br />
  _thread<br />
  matplotlib<br />
## Functions and keywords
### Functions 功能
Send training information to wechat every epoch(auto)  

每个epoch自动发送训练信息  
<br />  
  
Send figures to wechat every epoch(auto)  

每个epoch自动发送图表  
<br />  
  
Get figures manualy  

主动获取图表  
<br />  
  
Shut down/cancel computer  

关机/取消关机  
<br />  
  
Specify a stop epoch  

指定训练停止epoch数  
<br />  
  
Stop now manualy  

立刻停止训练(当前epoch结束后)  
<br /><br />
New：Get gpu status<br />
新增：获取GPU状态<br /><br />新增：查询进度<br />
### Keywords/commands 关键词和命令
stop_training_cmdlist=['Stop now',"That's enough",u'停止训练',u'放弃治疗']  

The keywords of stop training,if any of them is in the msg you sent,the command would be accepted  

停止训练的关键词列表，发送的消息中包含任意一项都可触发命令  
<br />  
  
shut_down_cmdlist=[u'关机','Shut down','Shut down the computer',u'别浪费电了',u'洗洗睡吧']  

The keywords of shutting down,similair to stop_training_cmdlist  

关机关键词列表，和stop_training_cmdlist类似  
<br />  
  
cancel_cmdlist=[u'取消','cancel','aaaa']  

The keywords of cancel shutting down,similair to stop_training_cmdlist  

取消关机关键词列表，和stop_training_cmdlist类似  
<br />  
  
get_fig_cmdlist=[u'获取图表','Show me the figure']   

The keywords of getting figure,similair to stop_training_cmdlist  

获取图表关键词列表，和stop_training_cmdlist类似  
<br />  
  
specify stop epoch:  

keywords:'Stop at + epoch'  

指定训练停止轮数  
<br /><br />
gpu_cmdlist=['GPU','gpu',u'显卡']<br />
type_list=['MEMORY', 'UTILIZATION', 'ECC', 'TEMPERATURE', 'POWER', 'CLOCK', 'COMPUTE', 'PIDS', 'PERFORMANCE', 'SUPPORTED_CLOCKS,PAGE_RETIREMENT', 'ACCOUNTING']<br />显卡关键词
  以及可查询状态列表<br /><br />prog_cmdlist=[u'进度','Progress']<br />查询进度，预告停止时间<br />Get progress，preview stop time
## Examples
specify stop epoch  

指定训练停止轮数  
<br />
Example:send:'Stop at:8' from your phone,and then training will be stopped after epoch8<br />
例如：手机发送“Stop at：8”，训练将在epoch8完成后停止<br /><br />
Stop training after current epoch finished<br />
当前epoch完成后停止训练<br />
example：send:'Stop now' or send:'停止训练' from your phone,and then training will be stopped after current epoch<br />
例如：手机发送“停止训练”或者“Stop now”，训练将会在当前epoch完成后被停止<br /><br />
Shutting down the computer after specified sec，specify waiting seconds and saved model filename by {sec} and [name](without .h5)<br />
在指定秒数后关机，用{sec}和[name]指定等待时间和保存文件名,文件名不包括.h5<br />
example:send:'Shut down now [test]{120}' from phone,the computer will be shut down after 120s,and save the model as test.h5<br />
or send:'Shut down now{120},don't save',then the model won't be saved.<br /><br />
Cancel shutting down the computer<br />
example：send:'取消关机' or 'cancel' from phone<br /><br />
Get figure of train infomation,specify metrics and level you want to show by[metrics]and{level},defualt are both 'all'<br />
example:send:'Show me the figure [loss]{batches}' from phone,you will recive a jpg image of losses in batches<br />
send:'Show me the figure'，you will recive two jpg images of all metrics in batches and epochs<br />
获取图表，通过[metrics]和{level}指定参数，如果没有指定则皆默认为’all'<br />
例如，手机发送"获取图表[loss]{batches}",会收到一个jpg格式的loss随batches变化的图片<br />
手机发送"获取图表",则会得到两张图片，分别是所有指标随batch和epoch的变化<br /><br />获取gpu状态<br />发送'gpu[MEMORY]'或者'GPU[MEMORY TEMPERATURE]'或者'显卡[MEMORY]'<br />
