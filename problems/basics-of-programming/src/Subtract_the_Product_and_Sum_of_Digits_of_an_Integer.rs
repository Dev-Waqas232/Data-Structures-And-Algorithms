fn main() {
    let n = 4421;
    println!("{}", subtract_product_and_sum(n));
}

fn subtract_product_and_sum(mut n: i32) -> i32 {
    let mut sum = 0;
    let mut product = 1;

    while n > 0 {
        product = product * (n % 10);
        sum = sum + (n % 10);

        n = n / 10;
    }

    return product - sum;
}
