// wget https://repo1.maven.org/maven2/org/alloytools/org.alloytools.alloy.dist/6.2.0/org.alloytools.alloy.dist-6.2.0.jar into sister directory libs

// jenv local 17.0.16
// run this with 
// javac -cp ../bin/org.alloytools.alloy.dist-6.2.0.jar InstanceGenerator.java
// java -cp .:../bin/org.alloytools.alloy.dist-6.2.0.jar InstanceGenerator model.als scopeNum

// generates an .xml instance of model.als for each scope of 0 .. scopeNum inclusive
// if no instance generated then no file written and the model is unsat at that scope


import java.io.File;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Element;

import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.io.PrintStream;
import java.io.OutputStream;

import edu.mit.csail.sdg.alloy4.A4Reporter;
import edu.mit.csail.sdg.alloy4.XMLNode;

import edu.mit.csail.sdg.ast.Sig;
import edu.mit.csail.sdg.ast.Sig.PrimSig;
import edu.mit.csail.sdg.ast.Sig.Field;

import edu.mit.csail.sdg.parser.CompModule;
import edu.mit.csail.sdg.parser.CompUtil;

import edu.mit.csail.sdg.translator.A4Options;
import edu.mit.csail.sdg.translator.A4Solution;
import edu.mit.csail.sdg.translator.A4SolutionReader;
import edu.mit.csail.sdg.translator.A4Tuple;
import edu.mit.csail.sdg.translator.A4TupleSet;
import edu.mit.csail.sdg.translator.TranslateAlloyToKodkod;

import kodkod.ast.Relation;


public class InstanceGenerator {

    //private static final String RUN_CMD_FORMAT = "run {} for exactly %d";
    private static final String INSTANCE_NAME_FORMAT = "%s-instance-%d.xml";

    private static String getCmd(List<String> topLevelSigs, Integer scope) {
        String sc = String.valueOf(scope);
        return "run {} for "+sc + " but " +
                    topLevelSigs.stream()
                        .map(s -> "exactly "+sc+" " + s)
                        .collect(Collectors.joining(", "));

    }

    public static void main(String[] args) throws Exception {

        if (args.length != 2) {
            System.err.println("FAIL: Args required: modelfileName scope");
            System.exit(1);
        }

        String modelFileName = args[0];
        // get absolutePath for file
        Path path = Path.of(modelFileName);  
        Path absolutePath = path.toAbsolutePath();
        String fullFileName = absolutePath.toString();
        String outputFileNamePrefix =
                fullFileName.substring(0, fullFileName.lastIndexOf("."));
        if (!Files.exists(absolutePath)) {
            System.out.println("File does not exist: " + fullFileName);
            System.exit(1);
        }

        Integer scope = Integer.parseInt(args[1]);
        if (! (scope >= 0)) {
            System.out.println("Scope must be >= 0");
            System.exit(1);
        }

        // read the contents of the input .als model
        String modelString = "";
        try {
            modelString = Files.readString(absolutePath, StandardCharsets.UTF_8);
        } catch (Exception e) {
            System.out.println("FAIL: Reading "+modelFileName +" failed with\n" + e.getMessage());
            System.exit(1);
        }

        List<String> topLevelSigs = new ArrayList<String>();
        
        A4Reporter rep = A4Reporter.NOP;
        
        try {
            CompModule modelWorld = CompUtil.parseEverything_fromString(rep, modelString);
            for (Sig sig : modelWorld.getAllReachableSigs()) {
                if (sig.isTopLevel() && !sig.builtin) {
                    topLevelSigs.add(sig.label.replace("this/",""));
                }
            }
        } catch (Exception e) {
            System.out.println("FAIL: Alloy jar failed to parse model with message\n" + e.getMessage());
            System.exit(1);
        } 

        try {
            A4Options opt = new A4Options();
            A4Solution sol;
            for (int k=0; k <= scope; k++) {
                String cmd = getCmd(topLevelSigs,k);
                //System.out.println(cmd);
                String modelPlusCmd = modelString + cmd;
                //System.out.println(modelPlusCmd);
                String instanceFileName;
                CompModule modelPlusCmdWorld = CompUtil.parseEverything_fromString(rep, modelPlusCmd);
                // because we added one to it
                int modelNumCmds = modelPlusCmdWorld.getAllCommands().size();
                // suppress kodkod messages
                System.setProperty("org.slf4j.simpleLogger.log.kodkod.engine.config", "warn");
                sol = TranslateAlloyToKodkod.execute_command(
                    rep, 
                    modelPlusCmdWorld.getAllReachableSigs(), 
                    modelPlusCmdWorld.getAllCommands().get(modelNumCmds-1), 
                    opt); 
                // it might not be satisfiable at one scope, but is satisfiable at the next scope
                System.out.println("satisfiable: " + sol.satisfiable());
                if (sol.satisfiable()) {
                    instanceFileName = "test.xml"; // INSTANCE_NAME_FORMAT.formatted(outputFileNamePrefix, k);
                    System.out.println(sol);
                    sol.writeXML(instanceFileName);
                    System.out.println("Wrote: "+ instanceFileName);
                }
            }
        } catch (Exception e) {
            System.out.println("FAIL: Alloy jar failed to parse model with cmd with message\n" + e.getMessage());
            System.exit(1);
        }        
    }

}
    
    



