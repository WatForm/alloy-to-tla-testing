{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable"; # this provides the ability to update dependencies, but no update happens unless flake.lock is modified explicitly. This does not imply that the dependencies themselves are bug-prone
    flake-utils.url = "github:numtide/flake-utils"; # used to generalize for all hardware
  };

  outputs =
    { self, nixpkgs, flake-utils, ... }:
    
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system}; # this refers to the main nixpkgs repo, this does not imply that the packages themselves are outdated in any way
    in
    {
      devShells.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          alloy # enables the alloy5 command, which brings up the UI
          alloy6 # enables the alloy6 command, which brings up the UI
          tlaplus18 # running tla on the command line
        ];


        shellHook = ''
          echo "Welcome to the nix shell for dashplus testing!"
          echo "alloy5 -> run alloy 5 GUI"
          echo "alloy6 -> run alloy 6 GUI"
          echo "tlc -> run the TLA model checker on the command line"
        '';
      };
    });
}
