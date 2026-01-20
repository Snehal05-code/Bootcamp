def main() 
	ch = make(chan int, 2)
	ch <- 1
	ch <- 2
	print(<-ch)
	print(<-ch)
end