
from data import critics
from recommendations import pearson_correlation
from recommendations import pearson_correlation_formula

print pearson_correlation(critics, 'Lisa Rose', 'Jack Matthews');
print pearson_correlation_formula(critics, 'Lisa Rose', 'Jack Matthews');
