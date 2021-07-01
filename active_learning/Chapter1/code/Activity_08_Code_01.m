
%% Spezifikation
Rs = 100;
R1 = 1e3;
L1 = 4.7e-3;
C1 = 0.1e-6;
Resr = 6.5;          % Effektiver Serienwiderstand in Ohm
Vin = 1;

f = logspace(100, 1e6);     % Frequenzbereich

%% Berechnung von Z
Y1 = 1/R1;
Y2 = i*2*pi.*f*C1;
Y3 = 1./(Resr+i*2*pi.*f*L1);
Y = Y1 + Y2 + Y3;
Z = 1./Y;

%% Plotting
fig1 = figure(1)
set(gca, 'fontsize', 14);
yyaxis left
semilogx(f, real(Z))
ylabel('Re(Z) in \Omega');

yyaxis right
semilogx(f, imag(Z))
ylabel('Im(Z) in \Omega');

xlabel('Frequenz f in Hz');
grid on

%% Export figure
print(fig1, '../img/Activity_08_Fig_04', '-depsc')
