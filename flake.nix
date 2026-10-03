{
  description = "NeoSpleen font";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in
    {
      packages = forAllSystems (
        pkgs:
        let
          version = builtins.head (
            builtins.match ".*Version: \"([0-9.]+)\".*" (builtins.readFile ./NeoSpleen.sfd)
          );
          meta = {
            homepage = "https://github.com/mbwilding/NeoSpleen";
            license = pkgs.lib.licenses.ofl;
            platforms = pkgs.lib.platforms.all;
          };
          neospleen = pkgs.stdenvNoCC.mkDerivation {
            pname = "neospleen";
            inherit version;
            src = self;
            nativeBuildInputs = [
              (pkgs.python3.withPackages (ps: [ ps.fontforge ]))
            ];
            buildPhase = ''
              runHook preBuild
              python3 generate_fonts.py ttf
              runHook postBuild
            '';
            installPhase = ''
              runHook preInstall
              install -Dm644 fonts/*.ttf -t $out/share/fonts/truetype
              runHook postInstall
            '';
            meta = meta // {
              description = "NeoSpleen";
            };
          };
          neospleen-nerdfont = pkgs.stdenvNoCC.mkDerivation {
            pname = "neospleen-nerdfont";
            inherit version;
            dontUnpack = true;
            nativeBuildInputs = [ pkgs.nerd-font-patcher ];
            buildPhase = ''
              runHook preBuild
              for f in ${neospleen}/share/fonts/truetype/*.ttf; do
                nerd-font-patcher "$f" --complete --boxdrawing --no-progressbars --quiet
              done
              runHook postBuild
            '';
            installPhase = ''
              runHook preInstall
              install -Dm644 *.ttf -t $out/share/fonts/truetype
              runHook postInstall
            '';
            meta = meta // {
              description = "NeoSpleen Nerd Font";
            };
          };
        in
        {
          inherit neospleen neospleen-nerdfont;
          default = neospleen;
        }
      );

      overlays.default = final: _prev: {
        inherit (self.packages.${final.stdenv.hostPlatform.system}) neospleen neospleen-nerdfont;
      };

      devShells = forAllSystems (pkgs: {
        default = import ./shell.nix { inherit pkgs; };
      });
    };
}
