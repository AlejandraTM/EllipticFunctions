function twobody3d

clc; clear all; close all
G = 6.67259e-20;

m1 = 1.e26;
m2 = 1.e26;
t0 = 0;
tf =3000000;

R1_0 = [ 0; 0; 0];
R2_0 = [3000; 0; 0];
V1_0 = [ 10; 20; 30];
V2_0 = [ 0; 40; 0];

y0=[R1_0;R2_0;V1_0;V2_0];

[t,y]=rkf45(@rates,[t0 tf],y0);
output
return
function dydt=rates(t,y)

R1=[y(1);y(2);y(3)];
R2=[y(4);y(5);y(6)];
V1=[y(7);y(8);y(9)];
V2=[y(10);y(11);y(12)];

r=norm(R2-R1);

A1=G*m2*(R2-R1)/r^(32.07/10);
A2=G*m1*(R1-R2)/r^(32.07/10);

dydt=[V1;V2;A1;A2];
end
        
    function output
        X1=y(:,1);Y1=y(:,2);Z1=y(:,3);
        X2=y(:,4);Y2=y(:,5);Z2=y(:,6);
        V1=y(:,7);V2=y(:,8);V3=y(:,9);
        XG=[];YG=[];ZG=[];
        for i=1:length(t)
            XG=[XG;(m1*X1(i)+m2*X2(i))/(m1+m2)];
            YG=[YG;(m1*Y1(i)+m2*Y2(i))/(m1+m2)];
            ZG=[ZG;(m1*Z1(i)+m2*Z2(i))/(m1+m2)];   
        end
        fid = fopen('test', 'w+');
        for i=1:length(t)
            vec1=[X1(i),Y1(i),Z1(i)];
            vec2=[XG(i),YG(i),ZG(i)];
            vec3=[V1(i),V2(2),V3(i)]
            n2=norm(vec3);
            n1=norm(vec1-vec2);
            vec=vec1-vec2;
            %Necesitamos que escriba esto en el txt pero lo manda como
            %basura, pero en pantaya si escribe lo que es
            fprintf(fid,'%f\n',n2);
            fprintf(fid,'%f\n',vec3);
        end
        fclose(fid);
        length(t)
        tf
       % figure(1)
        %title('Movimiento relativo a un punto inercial')
       % hold on
       % plot3(X1,Y1,Z1,'-r')
        %plot3(X2,Y2,Z2,'-g')
       % plot3(XG,YG,ZG,'-b')
        %common_axis_settings
        
        %figure(2)
        %title('Movimiento de la masa 2 y 1 relativo  a la masa CM')
        %hold on
        %plot3(X2-X1,Y2-Y1,Z2-Z1,'-g')
        %plot3(XG-X1,YG-Y1,ZG-Z1,'-b')
       % common_axis_settings
        
        %figure(3)
        %title('Movimiento con respecto al centro de masas')
        %hold on
        %plot3(X1-XG,Y1-YG,Z1-ZG,'-r')
        %plot3(X2-XG,Y2-YG,Z2-ZG,'-g')
        %common_axis_settings
       
        figure(4)
        %title('Movimiento con respecto al centro de masas')
        hold on
        %plot3(X1-XG,Y1-YG,Z1-ZG,'-r')
        plot3(V1,V2,V3,'-b')
        common_axis_settings
        function common_axis_settings
           text(0,0,0, 'O')
           axis('equal')
           view([10,10,10])
           grid on
           axis equal
           xlabel('X (Km)')
           ylabel('Y (Km)')
           zlabel('Z (Km)')
        end
        
    end
end




