{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    packages = with pkgs; [
        python312
        python312Packages.pip
        python312Packages.pyserial
        python312Packages.pyside6
        qt6.qtbase
    ];
}
