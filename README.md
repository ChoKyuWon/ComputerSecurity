## Computer Security
2020 Spring - 이호준 교수님

### Confued Deputy
ID와 Password를 입력받고 SHA256(password)가 passwd에 적힌 값과 일치하는지 확인한 뒤 같으면 플래그를 출력하고 다르면 ID를 이름으로 하는 파일에 입력한 비밀번호를 저장한다. 만일 ID를 passwd로 입력하면 기존의 passwd파일에 임의의 값을 입력할 수 있음으로 ID를 passwd로, 비밀번호를 원하는 임의의 문자열의 해시값을 넣어 passwd 파일을 조작한 뒤 다시 실행하면 플래그를 얻을 수 있다.
### Foward Secrecy
TLS1.2는 RSA를 사용하여 키를 공유할 수 있는데 이 때 서버 키가 Long Term이기 때문에 서버의 RSA private key가 노출된다면 이전의 캡처된 통신이 복호화 될 수 있는 단점이 있다. 이를 직접 볼 수 있는 문제로 캡처된 통신과 서버의 private key를 사용해 premaster를 복호화하고 premaster에서 직접 통신에 사용되는 AES 키를 derive 한 뒤 암호문을 복호화한다.
### Rock Scissor Paper
랜덤을 사용할 때 PRNG에 넣는 시드가 같다면 항상 같은 패턴으로 값이 도출된다
### Your First BOF
BOF로 쉘 코드를 버퍼에 넣고 리턴 어드레스를 쉘 코드의 처음으로 덮으면 된다
### Escape Room
ROP를 통해 임의의 주소에 임의의 값을 넣고 임의의 함수를 실행한다
### Ghost Student
코딩 실수를 통해 스택 카나리를 유출한다. 이후 리턴 어드레스 변조를 통해 임의 함수를 실행한다.
### Use After Free
로그인 한 뒤 그 유저를 삭제하고 msg를 할당받으면 그 공간에 임의 데이터를 쓸 수 있다. 이를 통해 권한을 변경할 수 있다.