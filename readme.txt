# git ����̳�

1��mkdir �ļ��������� -----> ����һ���ļ���

2��git init 	      -----> git��ʼ����ʹ��ǰ�ļ��г�Ϊgit���زֿ�

3��git add �ļ���     -----> ����ļ����ֿ�
	��git add -f��ǿ������ļ���

4��git commit -m "�Ķ���¼" -----> ��ӸĶ���¼���ύ˵��

5��git status -----> �鿴�ֿ⵱ǰ״̬

6��git diff �ļ��� -----> �鿴�޸�����

7��git log -----> �鿴���������Զ���ύ��־

8��git log --pretty=oneline

9��git reset --hard HEAD^ -----> ���˵���һ���汾
	HEAD^^���˵��������汾��HEAD~N���˵���N���汾

10��cat �ļ��� -----> �鿴�ļ�����

11��git reset --hard �汾��ǰ��λ -----> ����ָ���汾

12��git reflog -----> ��ʾ��¼��git����

13��git checkout -- �ļ��� -----> �����ļ��ڹ��������޸�

14��git rm �ļ��� -----> �ڰ汾����ɾ��ָ���ļ�


------------------ git Զ�̹���̳� ------------------------

1����Լ�git��������ע��GitHub�˺�

2��ssh-keygen -t rsa -C "�����ַ" -----> ����SSH Key

3����GitHub��վ"Account settings","SSH Keys"���"Add SSH Key"����������Title�����ı�����ճ��id_rsa.pub�ļ�������

4�����"Add Key" ������KEY

-------------- ����Զ��gitHub�ֿ� ----------------------

1����GitHub�е��"Create a new repo", ��Repository name�����ļ������ƣ��뱾�ر���һ�¿ɷ������

2��git remote add origin git@github.com:�˻���/�ļ���.git -----> �����زֿ���Զ�̹���

3��git push -u Զ�̿��� ���ط�֧ -----> �����ؿ��������͵�Զ�̿⣬-u ����ʹ���ط�֧��Զ�̷�֧���������Ժ�����

4��git clone git@github.com:�˺�/·��.git -----> ��Զ�̿��¡���ݵ����أ�����ֱ����git clone+��ַ ��¡Զ�̿⣩

5��git checkout -b ��֧�� -----> ����һ���µķ�֧���൱�ڣ�git branch ��֧��; git checkout ��֧����

6��git branch -----> �鿴��ǰ��֧

7��git merge ��֧�� -----> ��ָ����֧�ϲ�����ǰ��֧

8��git branch -d ��֧�� -----> ɾ��ָ����֧

9��git log --graph --pretty=oneline --abbrev-commit -----> �������鿴��֧�ϲ����

10��git merge --on---m "�ϲ�˵��" ��֧�� -----> --on--off��ʾ����Fast forward 

=====���� ˵����master��֧Ӧ�ñ����ȶ��������������°汾��Ҫ�����޸�ʱʹ�ñ�ķ�֧�޸ĺ��ٺϲ�

11��git stash -----> ���ص�ǰ�����ֳ������Ժ�ָ��ֳ��ɼ�����������ʱ���Դ����µķ�֧���޸Ĵ���

12��git stash list -----> �鿴���������Ĺ����ֳ�

13��git stash pop -----> �ָ�stash���ݣ�����stash����ɾ�����൱��git stash apply; git stash drop��

14��git stash apply stash@{N} -----> �ָ�ָ����stash

15��git remote -----> �鿴Զ�̿���Ϣ

16��git remote -v -----> �鿴����ץȡ�����͵�git��ַ

17��git pull -----> �����µ��ύץȡ���أ��ڱ��غϲ������ͻ��

18��git tag "��ǩ����" -----> ����ǰ��֧���ǩ

19��git tag "��ǩ����" �汾�� -----> ��ָ���汾���ǩ

20��git show "��ǩ����" -----> �忨��ǩ��Ϣ

21��git tag -d "��ǩ��" -----> ɾ��ָ����ǩ����ɾ������

22��git push Զ�ֿ̲� ��ǩ�� -----> ���ͱ�ǩ��Զ��
	��git push Զ�ֿ̲� --tags���������б�ǩ��Զ�̣�

23��git push Զ�ֿ̲� :refs/tags/��ǩ�� -----> ɾ��Զ�̱�ǩ������ɾ�����ر�ǩ

24��git remote rm Զ�̿��� -----> ɾ���ѹ�����Զ�̿⣨���ӵ��¿�ʱ�ã�



25��git config --global color.ui true -----> ����git��ʾ��ɫ


----------------- ���������ļ� -----------------------

1���ڹ�����Ŀ¼����".gitignore"�ļ������������ļ�����ֱ�������https://github.com/github/gitignore

�����ļ���ԭ���ǣ�

    1. ���Բ���ϵͳ�Զ����ɵ��ļ�����������ͼ�ȣ�
    2. ���Ա������ɵ��м��ļ�����ִ���ļ��ȣ�Ҳ�������һ���ļ���ͨ����һ���ļ��Զ����ɵģ����Զ����ɵ��ļ���û��Ҫ�Ž��汾�⣬����Java���������.class�ļ���
    3. �������Լ��Ĵ���������Ϣ�������ļ��������ſ���������ļ���

2��git check--ignore -v �ļ��� -----> ���������λ��

3��git config --global alias.������ ������ -----> ���������������git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"��


--------------------- �Git������ ---------------------

ǰ��Ҫ��1��׼��һ̨����Linux�Ļ���
	  2��ʹ��Ubuntu��Debian���Լ���apd������ɰ�װ

1��sudo apt-get install git -----> ��װgit

2��sudo adduser git -----> ����git�û�������git����

3������֤���½�������¼��yoghurt��Կid_rsa.pub���ݿ�����"/home/git/.ssh/authorized_keys"�ļ��һ��һ��

4��sudo git init --bare sample.git -----> ��ʼ��git�ֿ�
   sudo chown -R git:git samle.git -----> ��ֹ�û��ڷ������޸Ĺ���������owner��Ϊgit

5���༭"/etc/passwd"�ļ����ҵ�"git:x:1001:1001:,,,:/home/git:/bin/bash"�޸�Ϊ"git:x:1001:1001:,,,:/home/git:/user/bin/git-shell"��������git�û���������ͨ��sshʹ��git�����޷���½shell��

6��git clone git@server:/srv/sample.git -----> ��¡���������Լ�����





