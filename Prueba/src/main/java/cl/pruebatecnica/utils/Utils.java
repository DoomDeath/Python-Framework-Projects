package cl.pruebatecnica.utils;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Utils {

    public static boolean validarCorreo(String correo) {
        String regex = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(correo);
        return matcher.matches();
    }
    public static boolean validarPassword(String password) {
        String regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d{2}).{8,}$";
        return password.matches(regex);
    }

}
