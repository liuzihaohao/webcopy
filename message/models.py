from django.db import models
from uuid import uuid4

# Create your models here.
class messgaelist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    code=models.CharField(max_length=5,verbose_name='代码',unique=True)
    typetf=models.CharField(choices=(('t','text'),('f','file')),max_length=1,verbose_name="类型")
    file=models.FileField(upload_to='file/'+str(uuid4())+'/',verbose_name="文件",null=True, blank=True)
    text=models.TextField(max_length=4096,verbose_name="文本",null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='消息列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.code
class settingslist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    key=models.CharField(max_length=50,verbose_name='键',unique=True)
    val=models.CharField(max_length=100,verbose_name='值')
    oth=models.CharField(max_length=200,verbose_name='备注',null=True,blank=True)
    class Meta:
        verbose_name='设置参数'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.key
class filedellist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    filedir=models.TextField(max_length=4096,verbose_name="路径",null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='已删除文件'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.code