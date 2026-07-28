# dynamic report generator
def bold_text(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper
class Report:
    templates={}
    def __init__(self,title,content):
        self.title=title
        self.content=content
    @classmethod
    def add_template(cls,name,func):
        cls.templates[name]=func
    @classmethod
    def retrieve_template(cls,name):
        return cls.templates.get(name)
    def __call__(self,template_name):
        template=self.retrieve_template(template_name)
        if template:
            return(template(self))
        return 'template not found'
    def __str__(self):
        return f'title : {self.title}\ncontent : {self.content}'
def simple(report):
    return str(report)
@bold_text
def fancy(report):
     return "*****\n" + str(report) + "\n*****"
def main():
    Report.add_template("simple",simple)
    Report.add_template("fancy",fancy)
    report=Report('Monthly report','sales increased by x%')
    print(report('simple'))
    print()
    print(report('fancy'))
if __name__=='__main__':
    main()