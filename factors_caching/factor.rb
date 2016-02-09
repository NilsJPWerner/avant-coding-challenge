#!/usr/bin/ruby

def findFactors(numbers)
    # Outputs each integer in the array and all the other integers
    # in the array that are factors of the first integer.
    cache = factorToCache(numbers, Hash.new)
    output = "{"
    cache.each {|key, factors| output = output + "#{key}: #{factors}, "}
    output += "}"
    puts output
end


def factorToCache(array, cache)
    # Loop through array and first see if the value appears in the cache
    # If it doesn't pairwise check with every other value in the array
    # Assumptions:  That duplicates in the array and the factors are skipped
    #               In order to save computation time.
    for i in 0...array.length
        value = array[i]
        if !cache.has_value?(value)
            factors = []
            for j in 0...array.length
                pairwiseCheck(array[i], array[j], factors, cache)
            end
            cache[value] = factors
        end
    end
    return cache
end

def pairwiseCheck(value, pos_factor, factors, cache)
    # Check to see if pos_factor is a factor of pair 1
    # If it is see if pos_factor exists in the cache.
    # If so combine the cached pos_factor factors with the pair 1 factors
    # Then (regardless of previous if) add pos_factor to factors
    # Note that and short circuits so it wont have to evaluate the factor if
    # its found to be false earlier.
    if (value != pos_factor) and !(factors.include?(pos_factor)) and (value %
        pos_factor == 0)
        if cache.has_value?(pos_factor)
            factors = factors | cache[pos_factor]
        end
        factors.push(pos_factor)
    end
end


# findFactors([10, 5, 2, 20])
# findFactors([6, 7, 12, 123, 23, 65, 5, 12, 512, 126, 4, 7, 23, 5, 6])