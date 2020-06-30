% smbh_max_mass.m start

% script calculationg maximum mass for mass agregation through gezeitenkraefte

% constants in SI-units
RS =    695700000; % radius of sun in meter
MS =    1.9880e+30; % mass of sun in kilogram

% constants in planck units
RS = RS / (1.6 * 10^-35);
MS = MS / (2.18 * 10^-8);

% calculating max mass
MBH_max = (1.2 * RS / MS^(1/3))^1.5;

% bringing mass in SI units
MBH_max = MBH_max * (2.18 * 10^-8);

% mbh_max in terms of sun mass
MBH_max = MBH_max / 1.9880e+30


% smbh_max_mass.m end
