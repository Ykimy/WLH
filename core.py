import requests
from bs4 import BeautifulSoup

global course_info      #[{'url':'**', 'name':'**', 'undone_homework':'**', 'new_notice':'**', 'new_file':'**'}, ...]
course_info = []        #新版网络学堂url地址长度为76，旧版url为64
global course           #[{name:'**', notice:[{'rank':'**', 'title':'**', 'release':'**', 'time':'**', 'ifread':'**', 'content':'**', 'content':'**'},...],
                        # file:[{'rank':'**', 'title':'**', 'intro':'**', 'memory':'**', 'time':'**', 'state':'**', 'url':'**'}...],
                        # homework:['name':'**', 'release_time':'**', 'ddl': '**', 'ifsubmit': '**', 'memory': '**', 'title_url':'**',
                        # 'filename': '**', 'attachname': '**'], }, ...]
global s
course = []

def logIn(userid, userpass):     #抓取所有文本信息
    global s
    s = requests.session()                          #登录并且在主界面中抓取信息
    global login_data
    global course_info
    login_data = {'userid': userid, 'userpass': userpass}
    try:
        s.post('https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp', login_data)
        #s.post('https://learn.tsinghua.edu.cn/index.jsp', login_data)
        r = s.get('http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/MyCourse.jsp?language=cn')
    except:
        return (False, 1)  #错误代码1：网络未连接

    soup = BeautifulSoup(r.text, 'html.parser')
    if len(soup) == 0:
        return (False, 2)   #错误代码2：用户名或密码不正确

    tr_list = soup.find_all(name='tr', class_='info_tr2') + soup.find_all(name='tr', class_='info_tr')

    course_url = []                                 #利用主界面抓取的课程号构建所有url，并且存储主界面信息
    old_course_url = []                             #都是旧学堂url，只有course_url不是
    course_notice_url = []
    course_file_url = []
    course_homework_url = []
    for tr in tr_list:
        course.append({})
        tem = tr.get_text().split()
        course_info.append({'url': tr.a['href'], 'name': tem[0], 'undone_homework': tem[1], 'new_notice': tem[2], 'new_file': tem[3]})
        course_url.append(tr.a['href'])
    for i in range(len(course_url)):
        if len(course_url[i]) < 70:
            tem = course_url[i].split('?')
            old_course_url.append(course_url[i])
            course_notice_url.append('http://learn.tsinghua.edu.cn/MultiLanguage/public/bbs/getnoteid_student.jsp?' + tem[1])
            course_file_url.append('http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/download.jsp?' + tem[1])
            course_homework_url.append('http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/hom_wk_brw.jsp?' + tem[1])
        else:
            pass

    for i in range(len(old_course_url)):
        course[i]['notice'] = []            #notice:[{'rank':'**', 'title':'**', 'release':'**', 'time':'**', 'ifread':'**', 'content_url':'**', 'content':'**'},...]
        r = s.get(course_notice_url[i])     #notice
        tem_soup = BeautifulSoup(r.text, 'html.parser')
        course[i]['name'] = tem_soup.find(name='td', class_='info_title').text.split('\xa0')[1].split('\n')[0]
        notice = tem_soup.find_all(name='tr', class_='tr1') + tem_soup.find_all(name='tr', class_='tr2')
        for n in notice:
            tem = n.text.split('\n')
            for j in range(tem.count('')):
                tem.remove('')
            content_url = 'http://learn.tsinghua.edu.cn/MultiLanguage/public/bbs/' + n.a.get('href')
            course[i]['notice'].append({'rank': tem[0], 'title': tem[1], 'release': tem[2], 'time': tem[3], 'ifread': tem[4], 'content_url': content_url, 'content': ''})

        course[i]['file'] = []          # file:[{'rank':'**', 'title':'**', 'intro':'**', 'memory':'**', 'time':'**', 'state':'**', 'url':'**'}...]
        r = s.get(course_file_url[i])   # file
        tem_soup = BeautifulSoup(r.text, 'html.parser')
        file = tem_soup.find_all(name='tr', class_='tr1') + tem_soup.find_all(name='tr', class_='tr2')
        for f in file:
            tem = f.text.split('\n')
            for j in range(tem.count('')):
                tem.remove('')
            for j in range(len(tem)):
                tem[j] = tem[j].strip('\t')
                tem[j] = tem[j].strip('\r')
                tem[j] = tem[j].strip()
            for j in range(tem.count('')):
                tem.remove('')
            if tem[2][0] >= '0' and tem[2][0] <= '9':
                tem.insert(2, '')
            if len(tem) <= 5:
                tem.append('')
            url = 'http://learn.tsinghua.edu.cn' + f.a.get('href')
            course[i]['file'].append({'rank': tem[0], 'title': tem[1], 'intro': tem[2], 'memory': tem[3], 'time': tem[4], 'state': tem[5], 'url': url})

        course[i]['homework'] = []  # homework:['name':'**', 'release_time':'**', 'ddl': '**', 'ifsubmit': '**', 'memory': '**', 'title_url':'**', 'filename':'**', 'attachname':'**']
        r = s.get(course_homework_url[i])  # homework
        tem_soup = BeautifulSoup(r.text, 'html.parser')
        homework = tem_soup.find_all(name='tr', class_='tr1') + tem_soup.find_all(name='tr', class_='tr2')
        for h in homework:
            tem = h.text.split('\n')
            for j in range(tem.count('')):
                tem.remove('')
            for j in range(len(tem)):
                tem[j] = tem[j].strip('\t')
                tem[j] = tem[j].strip('\r')
                tem[j] = tem[j].strip()
            for j in range(tem.count('')):
                tem.remove('')
            url = 'http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/' + h.a.get('href')
            r = s.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            tem_filename = soup.find_all(name='td', class_='tr_2')[2]
            tem_attachname = soup.find_all(name='td', class_='tr_2')[4]
            filename = ''
            attachname = ''
            if len(tem_filename.contents) > 1:
                filename = tem_filename.a.text
            if len(tem_attachname.contents) > 1:
                attachname = tem_attachname.a.text
            course[i]['homework'].append({'name': tem[0], 'release_time': tem[1], 'ddl': tem[2], 'ifsubmit': tem[3],
                                          'memory': tem[4], 'title_url': url, 'filename': filename, 'attachname': attachname})
    old_course=[] 
    for c in course:
        if 'name' in c.keys():
            old_course.append(c)
    return (True, old_course)


def get_file(name, url, path=''):  #调用方式参考: get_file(name=course[0]['file'][0]['title'], url=course[0]['file'][0]['url'], path='F:\\')
    file = s.get(url, stream=True)
    tem_filename = file.headers.get('Content-Disposition')
    filename = tem_filename.split('=')[1]
    filename = filename.strip('"')
    filetype = filename.split('.')[1]
    with open(path + name + '.' + filetype, "wb") as code:
        code.write(file.content)

def get_homework_file(url, path=''):    #调用方式：get_homework_file(url=course[6]['homework'][1]['title_url'], path='F:\\')
    global s
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    file_url = soup.find(name='a').get('href')
    file = s.get('http://learn.tsinghua.edu.cn'+file_url, stream=True)
    filename = soup.find(name='a').text
    with open(path + filename, "wb") as code:
        code.write(file.content)

def get_notice_content(url):
    global s;
    r = s.get(url)
    content_soup = BeautifulSoup(r.text, 'html.parser')
    content = content_soup.find(name='td', class_='tr_l2', attrs={'style':"table-layout:fixed; word-break: break-all; overflow:hidden;"})
    if content.p != None:
        t = content
        content = ''
        for c in t.contents:
            if (c.name == 'td' or c.name == 'p')  and len(c.text) < 400:
                content += c.text
    else:
        content = content.text
    content = content.replace('\xa0', ' ')
    return content

def initial():
    global courses, course
    courses = []
    course = []

if __name__ == "__main__":
    courses = logIn("wangsiyu15", "wsy13579+")
    if courses[0]==False:
        if courses[1]==1:
            print("网络未连接")
        elif courses[1]==2:
            print("用户名或密码错误")
        exit()
    for course in courses:
        hws = course['homework']
        for hw in hws:
            if hw['filename'] != '':
                get_homework_file(hw['title_url'], "C:\\Users\\lenovo\\Desktop\\")
                exit()