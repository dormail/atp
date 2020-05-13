% skript fuer perioden dauer eines cepheiden
% Rechnung in si-Einheiten

% gravitationskonstante
G = 6.674 * 10^-11;

% einheiten ausgehend der sonne
rsun = 696000000;
msun = 1.9884 * 10^30;
au = 1.495 * 10^11;

% spezifische funktionen
% dichte einer kugel mit Radius R und Masse m
dense_sphere = @(R,m) m / (4 * pi * R^3 / 3);

% fuer diese aufgabe spezifische Werte eingesetzt
rho = dense_sphere(44.5 * rsun, 4.5 * msun);

% zeit die Schall von Zentrum bis Aussenhuelle des Cepheiden braucht
T = 1 / sqrt(2 * pi * G * rho /2);

% ausgabe der zeit des schalls in sekunden, stunden, tage
disp(T);
disp(T/3600);
disp(T/(3600*24));
