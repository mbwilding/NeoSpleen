{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.fontforge
    (pkgs.python3.withPackages (ps: [
      ps.fontforge
    ]))
  ];
}
