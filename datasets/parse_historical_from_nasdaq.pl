# parse historical quotes from http://www.nasdaq.com/
use strict;
use warnings;
 
my $filename = 'HSNIHistoricalQuotes.csv';
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";

my @serie;
my $max;
my $min;
my $i=-1;

while (my $row = <$fh>) {
 $i=$i+1;
	next if ($i<2);
  chomp $row;
  $row=~s/"//g;
  my @line=split /,/,$row;
  my $val=$line[1];
	push @serie,$val;
	if ($i==2)
	{
		$min=$val;
		$max=$min;
#		print "minmax initialized : $min $max\n";
	}
	else
	{
		if ($val > $max)
		{
			$max=$val;
		}
		if ($val<$min)
		{
			$min=$val;
		}
	}
  #print "$line[1]\n";
 
}

my $milieu=($max+$min)/2.0;
my $etendue=($max-$min)/2.0;
#print "min max $min $max\n";
foreach my $val (@serie)
{
	my $nized=($val-$milieu)/$etendue;
	print "$nized\n";
#	print "ZOO\n";

}