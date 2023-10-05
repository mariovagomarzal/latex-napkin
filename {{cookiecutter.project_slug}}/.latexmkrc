<% if cookiecutter.pythontex %>
# Support for pythontex
$clean_ext .= " pythontex-files-%R/* pythontex-files-%R";
push @generated_exts, 'pytxcode';

$pythontex = 'pythontex %O %S';
$extra_rule_spec{'pythontex'}  = [ 'internal', '', 'mypythontex', "%Y%R.pytxcode",  "%Ypythontex-files-%R/%R.pytxmcr",    "%R", 1 ];

sub mypythontex {
   my $result_dir = $aux_dir1."pythontex-files-$$Pbase";
   my $ret = Run_subst( $pythontex, 2 );
   rdb_add_generated( glob "$result_dir/*" );
   open( my $fh, "<", $$Pdest );
   if ($fh) {
      while (<$fh>) {
         if ( /^%PythonTeX dependency:\s+'([^']+)';/ ) {
	     print "Found pythontex dependency '$1'\n";
             rdb_ensure_file( $rule, $aux_dir1.$1 );
	 }
      }
      undef $fh;
   }
   else {
       warn "mypythontex: I could not read '$$Pdest'\n",
            "  to check dependencies\n";
   }
   return $ret;
}
<%+ endif %>
# Use luaLaTeX
<% if cookiecutter.pythontex or cookiecutter.minted %>
$pdflatex = 'lualatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
<% else %>
$pdflatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
<% endif %>
$pdf_mode = 1;

# Always compile
%go_mode = 1;
